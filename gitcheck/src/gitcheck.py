#!/usr/bin/env python3

from git import *
import configparser
import os
import sys
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Load configuration
# configuration has to be stored in $HOME/.gitcheck/gitcheck.conf
userHome = os.getenv("HOME")
if not userHome:
    logging.error("$HOME is not set - terminating ...")
    sys.exit(1)
logging.debug("User home: " + userHome)
CFG_PATH = userHome + "/.gitcheck/gitcheck.conf"
config = configparser.ConfigParser()
config.read(CFG_PATH)

logLevel = config.get("LOGGING","level")
if not logLevel in logging._nameToLevel:
    logging.error("Config error: bad logging level - terminating ...")
    sys.exit(0)
logging.getLogger().setLevel(logLevel)

dirsCfg = config.get("DIRS TO CHECK","dirs")
logging.debug("Dirs to be checked: " + dirsCfg)
if not dirsCfg:
    logging.info("No directories to be checked are configured - exiting ...")
    sys.exit(0)
dirs = dirsCfg.split('\n') # list of directories, each on separate line

# check each directory
for dir in dirs:
    repo = Repo(dir)
    logging.debug(repo.is_dirty())
    if len(repo.untracked_files) == 0:
        logging.info("No untracked files")
    else:
        logging.info("Untacked files:")
        for file in repo.untracked_files:
            logging.info("\t" + file)
