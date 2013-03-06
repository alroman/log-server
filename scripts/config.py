#!/bin/python
#
#   Loads a configuration file and parses the values
#

import ConfigParser
import logging
from datetime import date

# Logger for config module
logger = logging.getLogger('[config     ]')


class Config:

    def __init__(self):
        # expected config file
        self.cfgFile = 'config.cfg'

        try:
            with open(self.cfgFile) as f:
                # If we didn't raise an IO error, then file exists
                # attempt to load config vars
                f.close()
                self.loadConfig()

                logger.info("successfully loaded config")

        except IOError:
            # This means the file doesn't exist, or there was a problem loading it
            logger.error('%s file does not exist!', self.cfgFile)
            raise Error

        except ConfigParser.Error:
            # Raise our own exception
            logger.error('could not parse config file')
            raise Error

    def loadConfig(self):
        config = ConfigParser.RawConfigParser()
        config.read(self.cfgFile)

        # Load state
        self.pointer = config.getint('LogState', 'pointer')
        self.date = config.get('LogState', 'date')

        # Load DB settings
        self.host = config.get('Database', 'host')
        self.user = config.get('Database', 'user')
        self.passwd = config.get('Database', 'passwd')
        self.database = config.get('Database', 'database')

    def saveConfig(self, pointer):

        config = ConfigParser.RawConfigParser()
        config.add_section('LogState')
        config.set('LogState', 'pointer', pointer)
        config.set('LogState', 'date', self.today())

        # Save the config
        with open(self.cfgFile, 'wb') as configfile:
            config.write(configfile)

    def today(self):

        d = date.today()
        self.date = d.isoformat()
        return self.date


# Config exception
class Error(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
