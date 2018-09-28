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
#checks if any assets in the MD file structure have moved
#def checkAssetStructure(searchFolder):
#    for each line in dictionary.getStub():
#        realPath = Navi.findTargetFile(assetStub, searchFolder)
#        if(not(realPath == dictionary.getPath(assetStub))):
#            dictionary.setPath(assetStub, realPath)

def convertStubsToLinks(searchFolder):
    for root, dirs, files in os.walk(searchFolder):
        if("\.md" in files):
            mdFilePath = Navi.findTargetFile(files)
            with open(files, "r") as ins:
                for line in ins:
                    if(line.find("\[.*\]\(.*\)$")):
                        print("Found link\n")
                        tempStub = line
                        tempStub.replace( "^.*\[.*\]\((.*)\)$", "\1")
                        linkPath = dictionary.getPath(tempStub)
                        line.replace(tempStub, linkPath)
    return -1
