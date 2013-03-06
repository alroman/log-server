#!/bin/bash
#
# This script will take the mld_log SQL file and filter it so that
# only the INSERT rows are left in a convenient format

# cat log.sql | grep -E '\([0-9]+,.*\)' | sed 's|),(|),\n(|g' > temp.sql

# $1 = input file
# $2 = output file

# Expect timestamp file
DATE=`date +'%Y-%m-%d_%H%M'`
FILE_IN="$DATE.sql"
OUT_FILE="$DATE.out.sql"
POINTER="$3"

if [ -n "$1" ]; then
    FILE_IN=$1
fi

# Check if file exists
if [[ ! -e $FILE_IN ]]; then
    echo "1"
    # exit $?
fi

if [ -n "$2" ]; then
    OUT_FILE=$2
fi

# Create preliminary
echo "INSERT INTO \`mdl_log\` VALUES " > $OUT_FILE

# Run command
#   cat: This takes a raw mdl_log dump file
#   grep: filter out rows with pattern: (123, 1234567890, ...)
#   sed: separate the rows with neline, so that we get one row per line

cat $FILE_IN | grep -E '\([0-9]+,.*\)' | sed 's|),(|),\n(|g' | sed -e '1,/($POINTER,/d' >> $OUT_FILE

# cat $IN_FILE | sed -e '1,/($LINE,/d' >> $OUT_FILE

# exit status
echo $?

# Don't exit like this.. python doesn't like it!
# exit $?