#!/usr/bin/python

#----------------------------------------------------------------------
# Static Site Generator
# Program: showDocs
# Author: Ricky Dall'Armellina
# Date: 09/24/2018
#
# Description: checks if the first program argument is '-help' or if 
#              it's the first program execution to show the usuage docs
#----------------------------------------------------------------------

# Import statements
from .. import settings
import sys, os, webbrowser

TEXT_TO_WRITE = """The existance of this files tells the program it has been executed before.
Deleting this file will result in the program performing a first time execution and show the usage documentation.
You can also show the usage documentation by calling the program with the '-help' argument.
Thank you for using Flock!"""
USAGE_DOC = settings.PREFS_FOLDER + "docs/Flock-HowTo.html"

# Custom functions

def createFile():
    # creates the first time use file and adds the following contents to it
    f = open(settings.FIRST_USE_FILE, 'w+')
    f.write(TEXT_TO_WRITE)
    f.close()

def openDocs():
    # open usuage documentation with default browser
    settings.LOG("Opening usage documentation with the default web-browser\n")
    #webbrowser.open_new_tab(USAGE_DOC)
    webbrowser.open(USAGE_DOC, new=0, autoraise=True)

def showDocs(show):
    #print("Type '-help' when executing the program for usage guide\n")
    
    # check if firstUse file exists
    settings.LOG("Checking if first time use file exists: ")
    isFirstUse = os.path.isfile(settings.FIRST_USE_FILE)
    if not isFirstUse:
        # if not create it
        settings.LOG("File does not exist, creating it...\n")
        createFile()
        # open the documentation
        openDocs()
    else:
        settings.LOG("File exists\n")

    # check show flag
    if show == 1:
        # call show website
        openDocs()
    return
