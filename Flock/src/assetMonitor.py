#!/usr/bin/python3
#################################################
#    purpose: To update the locations of assets #
#             when changed by the user          #
#                                               #
#    Author: Dan Levy    Date:09/24/2018        #
#    Version: Initial                           #
#    Langauge: Python                           #
#################################################


from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import navigator.dirNaviV2 as Navi
import stubber.Stubber2 as dictionary
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
                                #print("Found link\n")
                                tempLine = line
                                tempLine = re.sub("^.*\[.*\]", "", tempLine)
                                parsedLine = re.split("[()]", tempLine)
                                tempStub = parsedLine[1]
                                stubInDict = False
                                for subString in parsedLine:
                                    for stub in stubList:
                                        if(subString == stub):
                                            stubInDict = True
                                            tempStub = subString
                                    if(stubInDict == False):
                                        #print("Stub, ", tempStub, ", not in dictionary")

                                    #Code block below extracts stub, gets the corresponding path from the dictionary
                                    #and replaces the stub in the line with the path from the dictionary
                                    linkPath = dictionary.getPath(tempStub)
                                    if(linkPath == -1):
                                        #print("Stub, ", tempStub, ", corresponding path not found in dictionary")
                                        #print("Substitution will not be carried out, check stubs in files for errors.")
                                    else:
                                        #Getting path of the link and replacing all "\" with "\\" to prevent \n, \t, etc.
                                        linkPath = re.sub(r"\\", r"\\\\", linkPath)
                                        linkPath = "(" + linkPath + ")"
                                        tempStub = "\(" + tempStub + "\)"
                                        line = re.sub(tempStub, linkPath, line)
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