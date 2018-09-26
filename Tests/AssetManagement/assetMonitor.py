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
#checks if any assets in the MD file structure have moved
def checkAssetStructure(searchFolder):
    for each line in dictionary.getStub():
        realPath = Navi.findTargetFile(assetStub, searchFolder)
        if(not(realPath == dictionary.getPath(assetStub))):
            dictionary.setPath(assetStub, realPath)

def convertAssetStubsToLinks(searchFolder):
    for root, dirs, files in os.walk(topDirectory):
        for each line in files:
            if(line.find("\[.*\]\(.*\)$")):
                tempStub = line
                string.replace(line, "^.*\[.*\]\((.*)\)$", "\1")
                return path
    return -1
