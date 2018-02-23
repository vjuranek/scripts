#!/usr/bin/env python3

from git import *
import configparser
import os,sys
import logging

# Setup logging
LOG_LEVELS = ["CRITICAL","ERROR","WARNING","INFO","DEBUG"]
logging.basicConfig(level=logging.INFO)

# Load configuration
# configuration has to be stored in $HOME/.gitcheck/gitcheck.conf
userHome = os.getenv("HOME")
if not userHome:
    print("$HOME is not set - terminating ...")
    sys.exit(1)
logging.debug("User home: " + userHome)
CFG_PATH = userHome + "/.gitcheck/gitcheck.conf"
config = configparser.ConfigParser()
config.read(CFG_PATH)

logLevel = config.get("LOGGING","level")
if not LOG_LEVELS.__contains__(logLevel):
    print("Config error: bad logging level - terminating ...")
    sys.exit(0)

dirsCfg = config.get("DIRS TO CHECK","dirs")
logging.debug("Dirs to be checked: " + dirsCfg)
if not dirsCfg:
    print("No directories to be checked are configured - exiting ...")
    sys.exit(0)
dirs = dirsCfg.split('\n') # list of directories, each on separate line

# check each directory
for dir in dirs:
    repo = Repo(dir)
    print(repo.is_dirty())
    if len(repo.untracked_files) == 0:
        print("No untracked files")
    else:
        print("Untacked files:")
        for file in repo.untracked_files:
            print("\t" + file)
