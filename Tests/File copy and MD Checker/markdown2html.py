#!/usr/bin/python

#----------------------------------------------------------------------
# Markdown to HTML Translator
# Author: Ricky Dall'Armellina
# Date: 09/3/2018
#
# Description: Translates a text file written in Markdown to a working
# HTML document and saves it with the same name
#----------------------------------------------------------------------
DEBUG = False

import os
import markdown
import markdown_extensions

def LOG(string):
    if DEBUG:
        print(string)

def getFileName(fileName):
    #get a substring with just the file name, no extension
    name = fileName[:-3]
    #print(name)
    return name

def checkExistingFile(fileName):
    htmlFileName = getFileName(fileName) + ".html"
    #check if file exits and delete it
    fileExists = os.path.isfile(htmlFileName)
    if fileExists:
        LOG("Removing previously created html file")
        os.remove(htmlFileName)
    else:
        LOG("HTML file doesn't exist, continuing...")

def generateHTMLHeader(file, mode):
    #generates html opening and closing elements
    #take the html file to ad headers to and a mode as an argument
    #mode 'o' (opening statements)
    #mode 'c' (closing statements)
    if mode == 'o':
        headFile = open("html_head.txt", "r", 0)
        file.write(headFile.read())
        headFile.close()
    elif mode == 'c':
        file.write("\n</body>\n</html>")
    return file

def createHTML(fileName):
    #get name from getFileName() and create html file with that name
    LOG("Creating HTML file...")
    htmlName = getFileName(fileName) + ".html"
    html = open(htmlName, "w+", 0)
    html = generateHTMLHeader(html, 'o')
    return html

def parseMarkdown(mFile, htmlFile):
    #call Markdown library to open the textFile and read it
    input_file = open(mFile, "r", 0)
    text = input_file.read()
    #input the contents of the markdown file into the html file
    html = markdown.markdown(text, ['markdown_extensions'])
    #write the converted html text to the html file
    htmlFile.write(html)
    return htmlFile

def markdown2html(inputFile):
    LOG("- Markdown to HTML Python Translator -\n")
    #create html file
    htmlFile = createHTML(inputFile)
    #parse and analyze the markdown file and obtain the html file
    outputFile = parseMarkdown(inputFile, htmlFile)
    generateHTMLHeader(outputFile, "c")
    return outputFile
