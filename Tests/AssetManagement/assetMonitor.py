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

import navigator.dirNaviV1 as Navi
import stubber.Stubber as dictionary
import string
import platform

def convertStubsToLinks(searchFolder):
    for root, dirs, files in os.walk(searchFolder):
        if("\.md" in files):
            topDir = platform.system
            mdFilePath = Navi.findTargetFile(files, topDir)
            with open(files, "r") as ins:
                for line in ins:
                    if(line.find("\[.*\]\(.*\)$")):
                        print("Found link\n")
                        tempStub = line
                        tempStub.replace( "^.*\[.*\]\((.*)\)$", "\1")
                        linkPath = dictionary.getPath(tempStub)
                        line.replace(tempStub, linkPath)
    return -1

