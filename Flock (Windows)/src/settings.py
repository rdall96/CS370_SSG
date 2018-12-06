#!/usr/bin/python
#----------------------------------------------------------------------
# Static Site Generator
# Author: Ricky Dall'Armellina
# Date: 11/13/2018
#
# Description: Settings file for Flock
#----------------------------------------------------------------------

import os
import re

DEBUG = False
# preferences directory path
PREFS_FOLDER = os.path.expanduser("~\.flock_preferences")
# create log directory
LOG_FILE = PREFS_FOLDER + "\\log\\"
FIRST_USE_FILE = PREFS_FOLDER + "firstUse"
DICTIONARY_FILE = PREFS_FOLDER + "flock_dictionary.txt"
THEMES_FOLDER = PREFS_FOLDER + "\Themes"

def LOG(string):

    global DEBUG
    LOG_FILE_FIXED = re.sub(':','-',LOG_FILE)
    LOG_FILE_FIXED = list(LOG_FILE_FIXED)
    LOG_FILE_FIXED[1] = ":"
    LOG_FILE_FIXED = "".join(LOG_FILE_FIXED)
    f = open(LOG_FILE_FIXED, "a+")
    f.write("\n" + string)
    f.close()

    if DEBUG:
        print(string)
    
    return

def createPreferencesFolder():
    
    global PREFS_FOLDER
    
    if not os.path.isdir(PREFS_FOLDER):
        os.mkdir(PREFS_FOLDER)
        os.mkdir(PREFS_FOLDER + "\log")
    
    return
