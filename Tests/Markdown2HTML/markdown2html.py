#!/usr/bin/python

#----------------------------------------------------------------------
# Markdown to HTML Translator
# Author: Ricky Dall'Armellina
# Date: 09/3/2018
#
# Translates a text file written in Markdown to a working HTML document
# and saves it with the same name
#----------------------------------------------------------------------
DEBUG = True

import sys
import os
#import markdown dictonary
import markdownDictonary as Markdown

def LOG(string):
    if DEBUG:
        print(string)

def checkExistingFile(fName):
    htmlFileName = getFileName(fName) + ".html"
    #check if file exits and delete it
    fileExists = os.path.isfile(htmlFileName)
    if fileExists:
        LOG("Removing previously created html file")
        os.remove(htmlFileName)
    else:
        LOG("HTML file doesn't exist, continuing...")

def getFileName(name):
    #get a substring with just the file name, no extension
    fName = name[:-4]
    #print(fName)
    return fName

def openText(fName):
    #open the file and return it
    #print("Opening file: ", fName)
    markText = open(fName, "r", 0)
    return markText

def createHTML(fName):
    #get name from getFileName() and create html file with that name
    LOG("Creating HTML file...")
    htmlName = getFileName(fName) + ".html"
    htmlText = open(htmlName, "w+", 0)
    htmlText.write("<!DOCTYPE html>\n")
    htmlText.write("<html><body>")
    return htmlText
def closeHTML(html):
    html.write("</body>")
    html.write("</html>")
    html.close()

def parseMarkText(text):
    #rename Markdown Dictonary for ease of use
    md = Markdown.dictonary
    for line in text:
        LOG(line)
        sliceString(line)
        

def sliceString(string):
    

#--------------------------------------------------------------------
#--------------------------------------------------------------------    

print("- Markdown to HTML Python Translator -\n")


# get a file name from the user
fileName = raw_input("Insert file name:")
#check for pre-existing html file
checkExistingFile(fileName)
#open the file
markText = openText(fileName)
#create html file
htmlText = createHTML(fileName)

#parse and analyze the markdown file
parseMarkText(markText)


#close the html file and add closing tags
closeHTML(htmlText)

