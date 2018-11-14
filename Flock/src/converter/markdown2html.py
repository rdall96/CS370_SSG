#!/usr/bin/python
#----------------------------------------------------------------------
# Markdown to HTML Translator
# Author: Ricky Dall'Armellina
# Date: 09/24/2018
#
# Description: Translates a text file written in Markdown to a working
#              HTML document and saves it with the same name.
#              Takes the full path of a markdown file and creates an
#              HTML file in the same location.
#              Returns true when successful and false when not.
#----------------------------------------------------------------------

from .. import settings
import os
import markdown
import markdown_extensions

FLOCK_HEADER_CODE = """<!DOCTYPE html>
<html><head>
<meta charset="utf-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" media="screen" href="styles.css"/>
</head></html>
<body>"""
FLOCK_FOOTER_CODE = """\n<a href="https://github.com/rdall96/Flock_SSG" target="blank" style="text-decoration:none;color:inherit;">
<div class="FlockFooter">
<p> Created using Flock   
<img src="flock_icon.png"/>
</p></div></a>\n</body>"""
EXTENSIONS_FILE = "src/converter/markdown_extensions.py"
EXECUTE_SUCCESSFULLY = False


def getFileName(fileName):
    # get a substring with just the file name, no extension
    name = fileName[:-3] # extension = '.md' 3 chars
    settings.LOG("File name: " + name)
    return name

def generateHTMLHeader(file, mode):
    # generates html opening and closing elements
    # take the html file to ad headers to and a mode as an argument
    # mode 'o' (opening statements)
    # mode 'c' (closing statements)
    if mode == 'o':
        file.write(FLOCK_HEADER_CODE)
    elif mode == 'c':
        file.write(FLOCK_FOOTER_CODE)
        # close the html file, done writing to it
        file.close()
    return file

def createHTML(fileName):
    # get name from getFileName() and create html file with that name
    settings.LOG("Creating HTML file...")
    htmlName = getFileName(fileName) + ".html"
    # Creates html file in the same location as the markdown file
    html = open(htmlName, "w+")
    # adds HTML header from html_head file
    html = generateHTMLHeader(html, 'o')
    # return HTML file object
    return html

def parseMarkdown(mFile, htmlFile):
    # try catch in case the file can't open, can't be read or can't be converted
    try:
        # open the textFile and read it
        settings.LOG("--- " + mFile)
        input_file = open(mFile, "r")
        # read inputFile as a string
        text = input_file.read()
        # converter returns an HTML string of text
        #html = markdown.markdown(text, [EXTENSIONS_FILE])
        html = markdown.markdown(text)
        # write the converted html text to the html file
        htmlFile.write(html)
        EXECUTE_SUCCESSFULLY = True
    except OSError as err:
        settings.LOG("Cannot open the target file: " + mFile)
        settings.LOG("Perhaps the path to the file is incorrect?")
        EXECUTE_SUCCESSFULLY = False
        settings.LOG(err)
    except ValueError:
        settings.LOG("Couldn't read the contents of the file")
        EXECUTE_SUCCESSFULLY = False
    except:
        settings.LOG("Unexpected error, could not convert the file")
        EXECUTE_SUCCESSFULLY = False
    return htmlFile

def markdown2html(inputFile):
    # inputFile is the full path to the file to convert
    settings.LOG("- Markdown to HTML Python Translator -\n")
    # create html file
    htmlFile = createHTML(inputFile)
    # parse and analyze the markdown file and obtain the html file
    outputFile = parseMarkdown(inputFile, htmlFile)
    # add closing headers for HTML
    generateHTMLHeader(outputFile, "c")
    # return if execute successfully or not
    return EXECUTE_SUCCESSFULLY

def checkIfValid(filePath):
    # takes the full path of a file to check if it is a valid .md file
    # returns true when file is valid, false when file is not
    fileExtension = filePath[:3]
    if fileExtension != ".md":
        settings.LOG("Selected file does not have a markdown (.md) extension")
        return False
    else:
        try:
            # create temporary html file to check if valid upon converison
            tempHTML = open("testHTML.html", "w+")
            tempHTML = parseMarkdown(filePath, tempHTML)
            # check if converted html file is empty
            if (os.stat(tempHTML).st_stat < 1):
                #if it's empty, then it wasn't a valid beginning file, because no content
                settings.LOG("Selected file is not a valid Markdown file")
                return False
            else:
                #file is not empty, so assuming it's valid html
                return True
        except:
            print("Unexpected error occured during valid markdown verification")
        # delete temporary html (tempHTML)
        tempHTML.close()
        os.remove("testHTML.html")
    return True

def convertAllMarkdown(folder):
    # Converts all markdown files in the selected directory
    filesConverted = 0 # number of files converted
    for root, dirs, files in os.walk(folder):
        for fileName in files:
            if fileName.endswith(".md"):
                filePath = os.path.join(root , fileName)
                # call conversion
                markdown2html(filePath)
                # add one to converted files counter
                filesConverted += 1
    settings.LOG(("Converted " + (str)(filesConverted) + " files"))
    return filesConverted