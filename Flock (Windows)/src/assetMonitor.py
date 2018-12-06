#!/usr/bin/python3
#################################################
#    purpose: To update the locations of assets #
#             when changed by the user          #
#                                               #
#    Author: Dan Levy    Date:09/24/2018        #
#    Version: Initial                           #
#    Langauge: Python                           #
#################################################

from . import settings
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import Flock.src.navigator.dirNaviV2 as Navi
import Flock.src.stubber.Stubber2 as dictionary
import string
import re
import os
#import requests
#checks if any assets in the MD file structure have moved
def checkAssetStructure(searchFolder):
    stubList = dictionary.getStubList()
    for stub in range(len(stubList)):
        realPath = Navi.findTargetFile(stub, searchFolder)
        if(not(realPath == dictionary.getPath(stub))):
            dictionary.changePath(stub, realPath)

#Regex http validation used in Django module implemented below
def isValidUrl(url):
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)

def convertStubsToLinks(searchFolder):
    stubList = dictionary.getStubList()
    for root, dirs, files in os.walk(searchFolder):
        for filename in files:
            if(".md" in filename):
                mdFilePath = os.path.join(root, filename)

                #Below opens Md file to parse lines and creates temp file to store new lines
                fh, absPath = mkstemp()
                with fdopen(fh,'w') as new_file:
                    with open(mdFilePath, "r+") as old_file:
                        for line in old_file:

                            #If statement below checks if the link syntax is in a line
                            if(re.search("\[.*\]\(.*\)", line, flags = 0)):
                                settings.LOG("Found link\n")
                                tempLine = line
                                tempLine = re.sub("^.*\[.*\]", "", tempLine)
                                parsedLine = re.split("[()]", tempLine)
                                tempStub = parsedLine[1]
                                stubInDict = False
                                for subString in parsedLine:
                                    #Below checks if subString is a valid URL
                                    if(not isValidUrl(subString)):
                                        for stub in stubList:
                                            if(subString == stub):
                                                stubInDict = True
                                                tempStub = subString
                                        if(stubInDict == False):
                                            settings.LOG("Stub, " + tempStub + ", not in dictionary")

                                        #Code block below extracts stub, gets the corresponding path from the dictionary
                                        #and replaces the stub in the line with the path from the dictionary
                                        linkPath = dictionary.getPath(tempStub)
                                        if(linkPath == -1):
                                            settings.LOG("Stub, " + tempStub + ", corresponding path not found in dictionary")
                                            settings.LOG("Substitution will not be carried out, check stubs in files for errors.")
                                        else:
                                            #Getting path of the link and replacing all "\" with "\\" to prevent \n, \t, etc.
                                            linkPath = re.sub(r"\\", r"\\\\", linkPath)
                                            linkPath = "(" + linkPath + ")"
                                            tempStub = "\(" + tempStub + "\)"
                                            line = re.sub(tempStub, linkPath, line)
                                    else:
                                        settings.LOG("\nWARNING: " + subString + " identified as a valid URL, no substitution carried out.\n")
                                #Write line to new Markdown file regardless of if it was changed        
                                new_file.write(line)
                            else:
                                new_file.write(line)
                #Deleting old MD file and moving new file to replace it
                remove(mdFilePath)
                move(absPath, mdFilePath)

    return -1
#These function calls below are for testing
#dictionary.populateDict(r"test_monitor")
#convertStubsToLinks(r"test_monitor")
