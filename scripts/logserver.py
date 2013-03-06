#!/bin/python

# http://amoffat.github.com/sh/
from sh import bash, grep, cat, cd
import sys
import os
import logging

# Set the sytem path to current directory so that we can load our own modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

import config

# Set up logging
logger = logging.getLogger('[log server]')


class LogServer:
    def __init__(self, cfg):
        self.cfg = cfg
        self.infile = 'log.sql'
        self.outfile = 'out.sql'

    def processLog(self):
        logger.info("starting to process sqldump file")

        # Bash scripts are in 'data' folder
        cd('data')

        # get the pointer
        pointer = self.findPointer()
        logger.info("> found pointer in file")

        return
        # Try to process this file
        output = bash('clean_sql.sh', self.infile, self.outfile, pointer)

        if int(output.trim()) == 0:
            raise Exception

        logger.info("> created out file")
        logger.info("finished processing sqldump file")

    def findPointer(self):
        for i in range(self.cfg.pointer, self.cfg.pointer + 100):

            pattern = '(' + str(i) + ','
            matches = grep(cat(self.infile), '-c', pattern)

            if int(matches.strip()) == 1:
                # Update the pointer
                self.cfg.pointer = i

                return i

        # If we get here, then we didn't find our pointer
        raise LogServerError

    def buildDb(self):
        # mysql('-u', self.cfg.user, '-p', self.cfg.passwd, selfcfg.dbname, _in=self.sqlfile)
        logger.info("nothing to do here...")


# Exceptions
class LogServerError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class LogServerProcessError(LogServerError):
    def __init__(self, value):
        self.value = value


def main():
    # Set up logger module
    # logging.basicConfig(filename='logserver.log',
    #                     level=logging.INFO,
    #                     format='%(asctime)s [%(name)s]  %(levelname)s: %(message)s',
    #                     datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(name)s  %(levelname)s: %(message)s',
                        datefmt='%m-%d-%Y %I:%M:%S %p')

    logger.info('START log procesing')

    try:
        # Load config settings
        cfg = config.Config()

        ls = LogServer(cfg)
        ls.processLog()

    except config.Error:
        logger.error('error loading config')
    except LogServerError:
        logger.error('log server error')

    logger.info('END log procesing')


if __name__ == "__main__":
    main()
