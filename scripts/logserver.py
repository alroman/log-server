#!/bin/python

# http://amoffat.github.com/sh/
from sh import bash, mysql
import sys
import os

# Set the sytem path to current directory so that we can load our own modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

import config

# Want this:
# cat log.sql | grep -E '\([0-9]+.*\)' | awk 'gsub("\),", "),\n")' | sed '/^$/d' > log_parsed.sql
# Algorithm:
#   get current record pointer and last filename
#   take log file from /path
#   clean the log file
#   find record pointer in file
#   trim all records up to that file
#
#
# cat log.sql | grep -E '\([0-9]+,.*\)' | sed 's|),(|),\n(|g' > temp.sql

# output = sed(awk(grep(cat(_in='log.sql'), '-E', '\([0-9]+.*\)'), 'gsub("\),", "),\n")'), '/^$/d', _out='log_parsed3.sql')
# print output.exit_code

# grep = grep.bake('-E')
# # sed = sed.bake("")
# output = sed(grep(cat('log.sql'), '\([0-9]+.\,*\)'), 's|),(|),\n(|g', _out='temp.sql')
# print output.exit_code

# command = "cat log.sql | grep -E '\([0-9]+,.*\)' | sed 's|),(|),\n(|g' > temp.sql"
# output = bash('log.sh', 'log.sql', 'temp.sql')


class LogServer:
    def __init__(self):
        print "foo"

    def getState(self):
        # Connect to database
        print "foo"

    def buildDb(self):
        mysql('-u', cfg.user, '-p', cfg.passwd, cfg.dbname, _in=self.sqlfile)


def main():
    print "[Log server] init"

    try:
        # Load config settings
        cfg = config.Config()

        print cfg.pointer
        print cfg.database

        log = LogServer()
        log.buildDb()

    except config.Error:
        print "- [Config Exception] There was a config error"

if __name__ == "__main__":
    main()
