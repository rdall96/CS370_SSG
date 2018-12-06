#!/usr/bin/python
#----------------------------------------------------------------------
# Static Site Generator
# Author: Ricky Dall'Armellina
# Date: 11/13/2018
#
# Description: Settings file for Flock
#----------------------------------------------------------------------

import os

DEBUG = False
# preferences directory path
PREFS_FOLDER = os.path.expanduser("~/.flock_preferences/")
# create log directory
LOG_FILE = PREFS_FOLDER + "log/"
FIRST_USE_FILE = PREFS_FOLDER + "firstUse"
DICTIONARY_FILE = PREFS_FOLDER + "flock_dictionary.txt"
THEMES_FOLDER = PREFS_FOLDER + "Themes/"

def LOG(string):

    global DEBUG

    f = open(LOG_FILE, "a+")
    f.write("\n" + string)
    f.close()

    if DEBUG:
        print(string)
    
    return

def createPreferencesFolder():
    
    global PREFS_FOLDER
    
    if not os.path.isdir(PREFS_FOLDER):
        os.mkdir(PREFS_FOLDER)
        os.mkdir(PREFS_FOLDER + "log/")
    
    return
