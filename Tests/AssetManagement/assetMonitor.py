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
import dirNaviV2 as Navi
import Stubber2 as dictionary
import string
import re
import os
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
                topDir = "assets"
                mdFilePath = os.path.join(root, filename)
               #Below opens Md file to parse lines and creates temp fiel to store new lines
                fh, absPath = mkstemp()
                with fdopen(fh,'w') as new_file:
                    with open(mdFilePath, "r+") as old_file:
                        for line in old_file:
                            #If statement below checks if the link syntax is in a line
                            if(re.search("\[.*\]\(.*\)", line, flags = 0)):
                                print("Found link\n")
                                parsedLine = re.split("[()]", line)
                                tempStub = parsedLine[1]
                                stubInDict = False
                                for stub in stubList:
                                    if(tempStub == stub):
                                        stubInDict = True
                                if(stubInDict == False):
                                    print("Stub, ", tempStub, ", not in dictionary")
                                tempLine = line
                                #Getting path of the link and replacing all "\" with "\\" to prevent \n, \t, etc.
                                linkPath = dictionary.getPath(tempStub)
                                linkPath = re.sub(r"\\", r"\\\\", linkPath)
                                print("Path of link is ", linkPath)
                                #Code block below extracts stub, gets the corresponding path from the dictionary
                                #and replaces the stub in the line with the path from the dictionary
                                if(linkPath == -1):
                                    print("Stub, ", tempStub, ", corresponding path not found in dictionary")
                                    print("Substitution will not be carried out, check stubs in files for errors.")
                                    new_file.write(line)
                                else:
                                    tempLine = re.sub(tempStub, linkPath, tempLine)
                                    new_file.write(tempLine)
                                print(tempLine)
                            else:
                                new_file.write(line)
                #Deleting old MD file and moving new file to replace it
                remove(mdFilePath)
                move(absPath, mdFilePath)

    return -1
#These function calls below are for testing
#dictionary.populateDict(r"assets")
#convertStubsToLinks(r"assets")