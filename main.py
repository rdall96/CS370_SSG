#!/usr/bin/python

#----------------------------------------------------------------------
# Static Site Generator
# Author: Ricky Dall'Armellina
# Date: 09/6/2018
#
# Description: This application takes a folder of markdown files and
#              translates them to a working HTML website, creating a
#              separate folder with the correct hierarchy.
#----------------------------------------------------------------------

DEBUG = True

# Import statements
import os
import src.converter.markdown2html as Converter
import src.stubber.Stubber as Stubber
import src.navigator.dirNaviV1 as DirNavigator

# Other functions

def LOG(string):
    if DEBUG:
        print(string)

def getSourcePath():
    LOG("Insert path to markdown documents: ")
    return raw_input()

def getDestinationPath():
    LOG("Insert path to the website folder: ")
    return raw_input()

def selectTheme():
    LOG("Choose a theme: \n 1. Light theme\n 2. Dark theme\n 3. Fun theme")
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
    return "Themes/" + theme + ".css"

def addStubs(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            LOG(file)
            if file.endswith(".md"):
                Stubber.stubGen(folder + '/' + file)
            else:
                LOG("Not a markdown file, skipping it...")

#----------------------------------------------------------------------
#----------------------------------------------------------------------
print(" - Welcome to the Static Site Generator! - ")

# Ask user for folder path with markdown files
markdownFolder = os.path.abspath(getSourcePath())
htmlFolder = os.path.abspath(getDestinationPath())

# Ask user to pick a theme for the website
userTheme = selectTheme()


# Analyze folder and build stub dictonary # Call Stubber
addStubs(markdownFolder)

# Create 'HTML' folder with same hierarchy as 'Markdown' folder


# Copy files to 'HTML' folder
# If the file's extension is '.md' then convert it

# Copy stylesheet
#DirNavigator.transcriptTargetFile(os.path.abspath(userTheme), os.path.abspath(htmlFolder + "/styles.css"))