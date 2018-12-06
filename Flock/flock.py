#!/usr/bin/python
#----------------------------------------------------------------------
# Static Site Generator
# Author: Ricky Dall'Armellina
# Date: 09/27/2018
#
# Description: This application takes a folder of markdown files and
#              translates them to a working HTML website, creating a
#              separate folder with the correct hierarchy.
#----------------------------------------------------------------------

# IMPORTS
from src import settings
import datetime, time
import os, shutil, sys, webbrowser
import src.converter.markdown2html as Converter
import src.docs.showDocs as UsageDocs
import src.stubber.Stubber2 as Stubber
import src.copier.fileCopy as Copier
import src.OScheckLooper as OSutil
import src.assetMonitor as Asset
import src.argChecker as ArgCheck
import src.themeSelector as Themer


# define log file name
settings.LOG_FILE += "flock_log-" + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H:%M:%S') + ".txt"
settings.createPreferencesFolder()

# FUNCTIONS

def getFullPath(folder):
    return os.path.abspath(folder + '/')

def checkExistingDestination(destinationFolder):
    # checking if user selected destination path is valid to save a website
    NEED_NEW_FOLDER = False # tells the program if it needs to request a new destination path

    settings.LOG("Checking if selected destination path already exists")
    pathExists = os.path.isdir(destinationFolder)
    if pathExists:
        print("Selected destination '" + destinationFolder + "' already contains a website folder.")
        checkDelete = input("Would you like to delete it? [yes/no] ")
        if checkDelete == 'y' or checkDelete == 'Y' or checkDelete == 'yes' or checkDelete == 'Yes' or checkDelete == 'YES':
            settings.LOG("Removing existing destination directory")
            shutil.rmtree(destinationFolder, ignore_errors=True)
            print("Folder removed")
        else:
            settings.LOG("Decided not to remove destination folder")
            print("Cannot proceed in this destination path")
            NEED_NEW_FOLDER = True # set this to tru to request new path upon return
    else:
        settings.LOG("Selected destination path is valid")
    return NEED_NEW_FOLDER

def renameIndex(folder):
    # renames index website file - file name needs to contain index as stub
    newName = folder + "/index.html"
    currName = (folder + "/" + Stubber.getPath("index")) # get path to file with stub index
    settings.LOG("   Index file: " + currName)
    # 11-27-2018 | os.rename() is deprecated since it does not work on Windows.
    # now using shutil.move() as a rename function
    shutil.move(currName, newName)
    # os.rename(currName, newName)
    return

#----------------------------------------------------------------------
#----------------------------------------------------------------------

print("\n - Welcome to Flock SSG - v1.0.1 beta - \n")

# Show usage docs if first time and check for arguments in command line
UsageDocs.showDocs(0)
ARG_RETURN = ArgCheck.parse(sys.argv)
if ARG_RETURN == True:
    # enable DEBUG
    settings.DEBUG = True

# Ricky Dall'Armellina - 12/06/2018 - Wrapping folder search in try catch to ensure stability when the folder path is not found
FOUND_FOLDER = False
while not FOUND_FOLDER:
    try:
        # Get path with markdown files from user
        markdownFolder = OSutil.systemCheck(input("Insert path to markdown documents: "))
        FOUND_FOLDER = True
        settings.LOG("Source folder:  " + markdownFolder)
    except:
        # could not find path, re-try
        FOUND_FOLDER = False
        print("Could not find a folder with the inserted name.")
        print("Please indicate the name of an existing folder.")

FOUND_FOLDER = False
while not FOUND_FOLDER:
    try:
        # Adding '/www' to the destination path to make sure it's an non-existing path to save the website
        htmlFolder = OSutil.systemCheck(input("Insert path to the website folder: ")) + "/www"
        FOUND_FOLDER = True
        # keep requesting new destination folder until path is okay to use
        while checkExistingDestination(htmlFolder):
            htmlFolder = OSutil.systemCheck(input("Insert path to the website folder: ")) + "/www"
        settings.LOG("Destination folder:  " + htmlFolder)
    except:
        # could not find path, re-try
        FOUND_FOLDER = False
        print("Could not find a folder with the inserted name.")
        print("Please indicate the name of an existing folder.")

# Create htmlFolder directory structure and copy files to it
settings.LOG("\ncopying files")
Copier.fileCopy(markdownFolder, htmlFolder)

# Call stub dictonary generation on destination folder
settings.LOG("\ngenerating dictonary")
indexedFiles = Stubber.populateDict(htmlFolder)
settings.LOG("   Indexed " + (str)(indexedFiles) + " files")

# Migrate links
settings.LOG("\nmigrating links")
Asset.convertStubsToLinks(htmlFolder)

# Convert files
settings.LOG("\nconverting files")
filesConverted = Converter.convertAllMarkdown(htmlFolder)
settings.LOG("   Converted " + (str)(filesConverted) + " files")

# Delete markdown files from destinantion
settings.LOG("\ndeleting original .md files from destination")
Copier.deleteMD(htmlFolder)

# Rename main website (index) file to "index.html"
settings.LOG("\nrenaming index file")
renameIndex(htmlFolder)

# Ask user to pick a theme for the website and copy it to destination folder
settings.LOG("\nselecting theme")
Themer.selectTheme(htmlFolder)

print("DONE!")

# Opening Website
website = htmlFolder + "/index.html"
webbrowser.open(website, new = 0, autoraise=True)
