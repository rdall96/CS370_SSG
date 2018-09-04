#!/usr/bin/python

#----------------------------------------------------------------------
# Markdown to HTML Translator
# Author: Ricky Dall'Armellina
# Date: 09/3/2018
#
# Description: Translates a text file written in Markdown to a working
# HTML document and saves it with the same name
#----------------------------------------------------------------------
DEBUG = True

import os
import markdown
import markdown_extensions

def LOG(string):
    if DEBUG:
        print(string)

def getFileName(name):
    #get a substring with just the file name, no extension
    fName = name[:-3]
    #print(fName)
    return fName

def checkExistingFile(fileName):
    htmlFileName = getFileName(fileName) + ".html"
    #check if file exits and delete it
    fileExists = os.path.isfile(htmlFileName)
    if fileExists:
        LOG("Removing previously created html file")
        os.remove(htmlFileName)
    else:
        LOG("HTML file doesn't exist, continuing...")

def createHTML(fileName):
    #get name from getFileName() and create html file with that name
    LOG("Creating HTML file...")
    htmlName = getFileName(fileName) + ".html"
    html = open(htmlName, "w+", 0)
    return html

def parseMarkdown(mFile, htmlFile):
    #call Markdown library to open the textFile and read it
    input_file = open(mFile, "r", 0)
    text = input_file.read()
    #input the contents of the markdown file into the html file
    html = markdown.markdown(text, ['markdown_extensions'])
    htmlFile.write(html)
    return htmlFile

#--------------------------------------------------------------------
#--------------------------------------------------------------------    

print("- Markdown to HTML Python Translator -\n")


# get a file name from the user
inputFile = raw_input("Insert file name:")
#check for pre-existing html file
checkExistingFile(inputFile)
#create html file
htmlFile = createHTML(inputFile)

#parse and analyze the markdown file and obtain the html file
outputFile = parseMarkdown(inputFile, htmlFile)
