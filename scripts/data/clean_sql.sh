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
FILE_OUT="$DATE.out.sql"

if [ -n "$1" ]; then
    FILE_IN=$1
fi

# Check if file exists
if [[ ! -e $FILE_IN ]]; then
    echo "1"
    # exit $?
fi

if [ -n "$2" ]; then
    FILE_OUT=$2
fi

# echo $FILE_IN
# echo $FILE_OUT

# Run command
cat $FILE_IN | grep -E '\([0-9]+,.*\)' | sed 's|),(|),\n(|g' > $FILE_OUT

# exit status
echo $?
# exit $?