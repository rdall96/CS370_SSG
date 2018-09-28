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
DEBUG = False

import os
import markdown
import markdown_extensions

HTML_HeaderFile = "html_head.txt"
EXECUTE_SUCCESSFULLY = False

def LOG(string):
    if DEBUG:
        print(string)

def getFileName(fileName):
    # get a substring with just the file name, no extension
    name = fileName[:-3] # extension = '.md' 3 chars
    LOG("File name: " + name)
    return name

def generateHTMLHeader(file, mode):
    # generates html opening and closing elements
    # take the html file to ad headers to and a mode as an argument
    # mode 'o' (opening statements)
    # mode 'c' (closing statements)
    if mode == 'o':
        headFile = open(HTML_HeaderFile, "r", 0)
        file.write(headFile.read())
        # close the header file
        headFile.close()
    elif mode == 'c':
        file.write("\n</body>")
        # close the html file, done writing to it
        file.close()
    return file

def createHTML(fileName):
    # get name from getFileName() and create html file with that name
    LOG("Creating HTML file...")
    htmlName = getFileName(fileName) + ".html"
    # Creates html file in the same location as the markdown file
    html = open(htmlName, "w+", 0)
    # adds HTML header from html_head file
    html = generateHTMLHeader(html, 'o')
    # return HTML file object
    return html

def parseMarkdown(mFile, htmlFile):
    # try catch in case the file can't open, can't be read or can't be converted
    try:
        # open the textFile and read it
        input_file = open(mFile, "r", 0)
        # read inputFile as a string
        text = input_file.read()
        # converter returns an HTML string of text
        html = markdown.markdown(text, ['markdown_extensions'])
        # write the converted html text to the html file
        htmlFile.write(html)
        EXECUTE_SUCCESSFULLY = True
    except OSError as err:
        LOG("Cannot open the target file: " + mFile)
        LOG("Perhaps the path to the file is incorrect?")
        EXECUTE_SUCCESSFULLY = False
        LOG(err)
    except ValueError:
        LOG("Couldn't read the contents of the file")
        EXECUTE_SUCCESSFULLY = False
    except:
        LOG("Unexpected error, could not convert the file")
        EXECUTE_SUCCESSFULLY = False
    return htmlFile

def markdown2html(inputFile):
    LOG("- Markdown to HTML Python Translator -\n")
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
        LOG("Selected file does not have a markdown (.md) extension")
        return False
    else:
        try:
            # create temporary html file to check if valid upon converison
            tempHTML = open("testHTML.html", "w+", 0)
            tempHTML = parseMarkdown(filePath, tempHTML)
            # check if converted html file is empty
            if (os.stat(tempHTML).st_stat < 1):
                #if it's empty, then it wasn't a valid beginning file, because no content
                LOG("Selected file is not a valid Markdown file")
                return False
            else:
                #file is not empty, soassuming it's valid html
                return True
        except:
            print("Unexpected error occured during valid markdown verification")
        # delete temporary html (tempHTML)
        tempHTML.close()
        os.remove("testHTML.html")
    return