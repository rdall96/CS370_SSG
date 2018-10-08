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

DEBUG = True

# Import statements
import os, shutil, sys
import src.converter.markdown2html as Converter
import src.docs.showDocs as UsageDocs
import src.stubber.Stubber2 as Stubber
import src.copier.fileCopy as Copier
import src.OScheckLooper as OSutil
import src.assetMonitor as Asset

# Other functions

def LOG(string):
    if DEBUG:
        print(string)
    return

def getFullPath(folder):
    return os.path.abspath(folder + '/')

def selectTheme(destFolder):
    print("Available themes: \n 1. Light theme\n 2. Dark theme\n 3. Fun theme")
    themeOption = raw_input("Choose a theme: ")
    if themeOption == '1':
        #light theme selected
        LOG("Light theme choosen")
        theme = "light_theme"
    elif themeOption == '2':
        #dark theme selected
        LOG("Dark theme choosen")
        theme = "dark_theme"
    elif themeOption == '3':
        #dark theme selected
        LOG("Fun theme choosen")
        theme = "fun_theme"
    else:
        LOG("The selected theme does not exist")
    themePath = "Themes/" + theme + ".css"
    shutil.copy2(themePath, (destFolder + "/styles.css"))
    return True


#----------------------------------------------------------------------
#----------------------------------------------------------------------

print("\n - Welcome to the Static Site Generator! - \n")
UsageDocs.showDocs(sys.argv)

# Ask user for folder path with markdown files
# call Lukes OS specific folder finder
markdownFolder = OSutil.systemCheck(raw_input("Insert path to markdown documents: "))
#LOG("Source folder:  " + markdownFolder)
# Adding '/www' to the destination path to make sure it's an non-existing path to save the website
htmlFolder = OSutil.systemCheck(raw_input("Insert path to the website folder: ")) + "/www"
#LOG("Destination folder:  " + htmlFolder)

# Create htmlFolder directory structure
    # Copy all files to it
#LOG("\ncopying files")
Copier.fileCopy(markdownFolder, htmlFolder)

# Call stub dictonary generation on destination folder
    # OS specific
#LOG("\ngenerating dictonary")
indexedFiles = Stubber.populateDict(htmlFolder)
LOG("   Indexed " + (str)(indexedFiles) + " files")

# Check if files are valid
    # Call Asset Monitor
#LOG("\nmigrating links")
Asset.convertStubsToLinks(htmlFolder)

# Convert files
#LOG("\nconverting files")
filesConverted = Converter.convertAllMarkdown(htmlFolder)
#LOG("   Converted " + (str)(filesConverted) + " files")
# Delete markdown files from destinantion
#LOG("\ndeleting original .md files from destination")
Copier.deleteMD(htmlFolder)

# Ask user to pick a theme for the website and copy it to destination folder
#LOG("\nselecting theme")
selectTheme(htmlFolder)

print("DONE!")
