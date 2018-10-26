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
DEBUG = False
def LOG(string):
    if DEBUG:
        print(string)
    return

# IMPORTS
import os, shutil, sys
import src.converter.markdown2html as Converter
import src.docs.showDocs as UsageDocs
import src.stubber.Stubber2 as Stubber
import src.copier.fileCopy as Copier
import src.OScheckLooper as OSutil
import src.assetMonitor as Asset
import src.argChecker as ArgCheck
import src.themeSelector as Themer

# FUNCTIONS

def getFullPath(folder):
    return os.path.abspath(folder + '/')

def checkExistingDestination(destinationFolder):
    # checking if user selected destination path is valid to save a website
    NEED_NEW_FOLDER = False # tells the program if it needs to request a new destination path
    
    LOG("Checking if selected destination path already exists")
    pathExists = os.path.isdir(destinationFolder)
    if pathExists:
        print("Selected destination '" + destinationFolder + "' already contains a website folder.")
        checkDelete = input("Would you like to delete it? [yes/no] ")
        if checkDelete == 'y' or checkDelete == 'Y' or checkDelete == 'yes' or checkDelete == 'Yes' or checkDelete == 'YES':
            LOG("Removing existing destination directory")
            shutil.rmtree(destinationFolder, ignore_errors=True)
            print("Folder removed")
        else:
            LOG("Decided not to remove destination folder")
            print("Cannot proceed in this destination path")
            NEED_NEW_FOLDER = True # set this to tru to request new path upon return
    else:
        LOG("Selected destination path is valid")
    return NEED_NEW_FOLDER

def renameIndex(folder):
    # renames index website file - file name needs to contain index as stub
    newName = folder + "/index.html"
    currName = (folder + "/" + Stubber.getPath("index")) # get path to file with stub index
    LOG("   Index file: " + currName)
    os.rename(currName, newName)
    return

#----------------------------------------------------------------------
#----------------------------------------------------------------------

print("\n - Welcome to the Static Site Generator! - \n")

# Show usage docs if first time and check for arguments in command line
UsageDocs.showDocs(0)
ARG_RETURN = ArgCheck.parse(sys.argv)
if ARG_RETURN == True:
    DEBUG = True

# Get path with markdown files from user
markdownFolder = OSutil.systemCheck(input("Insert path to markdown documents: "))
LOG("Source folder:  " + markdownFolder)
# Adding '/www' to the destination path to make sure it's an non-existing path to save the website
htmlFolder = OSutil.systemCheck(input("Insert path to the website folder: ")) + "/www"
# keep requesting new destination folder until path is okay to use
while checkExistingDestination(htmlFolder):
    htmlFolder = OSutil.systemCheck(input("Insert path to the website folder: ")) + "/www"
LOG("Destination folder:  " + htmlFolder)

# Create htmlFolder directory structure and copy files to it
LOG("\ncopying files")
Copier.fileCopy(markdownFolder, htmlFolder)

# Call stub dictonary generation on destination folder
LOG("\ngenerating dictonary")
indexedFiles = Stubber.populateDict(htmlFolder)
LOG("   Indexed " + (str)(indexedFiles) + " files")

# Migrate links
LOG("\nmigrating links")
Asset.convertStubsToLinks(htmlFolder)

# Convert files
LOG("\nconverting files")
filesConverted = Converter.convertAllMarkdown(htmlFolder)
LOG("   Converted " + (str)(filesConverted) + " files")

# Delete markdown files from destinantion
LOG("\ndeleting original .md files from destination")
Copier.deleteMD(htmlFolder)

# Rename main website (index) file to "index.html"
LOG("\nrenaming index file")
renameIndex(htmlFolder)

# Ask user to pick a theme for the website and copy it to destination folder
LOG("\nselecting theme")
Themer.selectTheme(htmlFolder)

print("DONE!")
