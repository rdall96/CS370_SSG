#!/usr/bin/python3
#################################################
#    purpose: To update the locations of assets #
#             when changed by the user          #
#                                               #
#    Author: Dan Levy    Date:09/24/2018        #
#    Version: Initial                           #
#    Langauge: Python                           #
#################################################
import os
import dirNaviV1 as Navi
import Stubber as dictionary
import string
import platform
#checks if any assets in the MD file structure have moved
def checkAssetStructure(searchFolder):
    stubList = dictionary.getStubList()
    for stub in range(len(stubList)):
        realPath = Navi.findTargetFile(stub, searchFolder)
        if(not(realPath == dictionary.getPath(stub))):
            dictionary.changePath(stub, realPath)

def convertStubsToLinks(searchFolder):
    for files in os.walk(searchFolder):
        if("\.md" in files):
            topDir = platform.system
            mdFilePath = Navi.findTargetFile(files, topDir)
            #Below opens Md file to parse lines
            with open(mdFilePath, "r+") as ins:
                for line in ins:
                    #If statement below checks if the link syntax is in a line
                    if(line.find("\[.*\]\(.*\)$")):
                        print("Found link\n")
                        #Code block below extracts stub, gets the corresponding path from the dictionary
                        #and replaces the stub in the line with the path from the dictionary
                        tempStub = line
                        tempStub.replace( "^.*\[.*\]\((.*)\)$", "\1")
                        linkPath = dictionary.getPath(tempStub)
                        line.replace(tempStub, linkPath)
    return -1

dictionary.p\