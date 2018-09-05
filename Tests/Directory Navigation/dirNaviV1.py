#!/usr/bin/python
#################################################
#    purpose: To explore recursive directory    #
#             navigation in python              #
#                                               #
#    Author: Dan Levy    Date:09/3/2018         #
#    Version: Initial                           #
#    Langauge: Python                           #
#################################################

import os
from os.path import join, getsize
def findTargetDir(targetDir):
    for root, dirs, files in os.walk('.'):
        print root, " is current directory",
        if targetDir in dirs:
            print targetDir, " found"
	    path = os.path.dirname(os.path.abspath(__file__))
	    return path
    return -1

def findTargetFile(targetFile)
    for root, dirs, files in os.walk('.'):
        print root, " is current directory",
        if targetFile in files:
            print targetFile, " found"
            path = os.path.dirname(os.path.abspath(__file__))
            return path
    return -1

