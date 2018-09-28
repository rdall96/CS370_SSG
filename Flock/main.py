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

# Import statements
import os, shutil, sys
import src.converter.markdown2html as Converter
import src.docs.showDocs as UsageDocs
import src.stubber.Stubber as Stubber
import src.copier.fileCopy as Copier

# Other functions

def LOG(string):
    if DEBUG:
        print(string)

def getFullPath(folder):
    return os.path.abspath(folder + '/')

def selectTheme(destFolder):
    print("Choose a theme: \n 1. Light theme\n 2. Dark theme\n 3. Fun theme")
    themeOption = raw_input()
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
        LOG("The selcted theme does not exist")
    themePath = "Themes/" + theme + ".css"
    shutil.copy2(themePath, (destFolder + "/styles.css"))

def addStubs(folder):
    for srcDir, dirs, files in os.walk(folder):
        for file_ in files:
            LOG(file_)
            if file_.endswith(".md"):
                Stubber.stubGen(srcDir + '/' + file_)
            else:
                LOG("Not a markdown file, skipping it...")


#----------------------------------------------------------------------
#----------------------------------------------------------------------

print("\n - Welcome to the Static Site Generator! - \n")
UsageDocs.showDocs(sys.argv)

# Ask user for folder path with markdown files
markdownFolder = getFullPath(raw_input("Insert path to markdown documents: "))
htmlFolder = getFullPath(raw_input("Insert path to the website folder: "))

# Create htmlFolder directory structure
    # Copy all files to it

# Call stub dictonary generation on destination folder
    # OS specific

# Check if files are valid
    # Call Asset Monitor

# Convert files

# Delete markdown files frm destinantion

# Ask user to pick a theme for the website and copy it to destination folder
#selectTheme(htmlFolder)

print("DONE!")
