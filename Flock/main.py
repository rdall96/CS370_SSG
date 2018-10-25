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

# FUNCTIONS

def getFullPath(folder):
    return os.path.abspath(folder + '/')

def renameIndex(folder):
    # renames index website file - file name needs to contain index as stub
    newName = folder + "/index.html"
    currName = (folder + "/" + Stubber.getPath("index")) # get path to file with stub index
    LOG("   Index file: " + currName)
    os.rename(currName, newName)
    return

def selectTheme(destFolder):
    # check if selected theme is valid, if not keep asking user for a valid theme
    isThemevalid = False
    while not isThemevalid:
        print("Available themes: \n 1. Light theme\n 2. Dark theme\n 3. Fun theme\n 4. Select your own")
        themeOption = input("Choose a theme: ")
        if themeOption == '1':
            #light theme selected
            LOG("Light theme choosen")
            theme = "light_theme"
            themePath = "Themes/" + theme + ".css"
            isThemevalid = True
        elif themeOption == '2':
            #dark theme selected
            LOG("Dark theme choosen")
            theme = "dark_theme"
            themePath = "Themes/" + theme + ".css"
            isThemevalid = True
        elif themeOption == '3':
            #dark theme selected
            LOG("Fun theme choosen")
            theme = "fun_theme"
            themePath = "Themes/" + theme + ".css"
            isThemevalid = True
        elif themeOption == "4":
            #custom user theme selected
            LOG("Custom user theme selected")
            themePath = input("Insert the path and name to your custom theme: ")
            isThemevalid = True
        else:
            LOG("The selected theme does not exist")
            print("\nPlease choose a valid theme")
    # copy stylesheet
    shutil.copy2(themePath, (destFolder + "/styles.css"))
    # copy Flock icon
    iconPath = "Themes/flock_icon.png"
    shutil.copy2(iconPath, (destFolder + "/flock_icon.png"))
    return True


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
selectTheme(htmlFolder)

print("DONE!")
