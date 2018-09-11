#!/usr/bin/python

#----------------------------------------------------------------------
# Static Site Generator
# Author: CS 370 group
# Date: 09/6/2018
#
# Description: This application takes a folder of markdown files and
#              translates them to a working HTML website, creating a
#              separate folder with the correct hierarchy.
#----------------------------------------------------------------------

DEBUG = True

# Import statements
import src.markdown2html as Converter

# Other functions

def LOG(string):
    if DEBUG:
        print(string)

def getSourcePath():
    LOG("Insert path to markdown documents: ")
    return raw_input()

def selectTheme():
    LOG("Choose a theme: \n 1. Light theme\n 2. Dark theme\n 3. Fun theme")
    themeOption = raw_input()
    if themeOption == '1':
        #light theme selected
        LOG("Light theme choosen")
        return "light_theme"
    elif themeOption == '2':
        #dark theme selected
        LOG("Dark theme choosen")
        return "dark_theme"
    elif themeOption == '3':
        #dark theme selected
        LOG("Fun theme choosen")
        return "fun_theme"
    else:
        LOG("The selcted theme does not exist")

#----------------------------------------------------------------------
#----------------------------------------------------------------------
print(" - Welcome to the Static Site Generator! - ")

# Ask user for folder path with markdown files
markdownFolder = getSourcePath()

# Ask user to pick a theme for the website
userTheme = selectTheme()

# Analyze folder and build stub dictonary


# Create 'HTML' folder with same hierarchy as 'Markdown' folder


# Copy files to 'HTML' folder
# If the file's extension is '.md' then convert it
