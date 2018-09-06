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

#Variables: targetDir is the directory to find
#           topDirectory is the directory you want to search all the children of
#Return Value(s): returns the absolute path of the target Directory, or -1 on failure
#Usage: targetDir must be passed in as a string containing the directory name
#       topDirectory msut be passed in as a string of the absolute path of the directory
def findTargetDir(targetDir, topDirectory):
    for root, dirs, files in os.walk(topDirectory):
        if targetDir in dirs:
            print targetDir, " found"
	    path = os.path.dirname(os.path.abspath(__file__))
            print " Path is ", path
	    return path
    return -1


def findTargetFile(targetFile, topDirectory):
    for root, dirs, files in os.walk(topDirectory):
        if targetFile in files:
            print targetFile, " found"
            path = os.path.dirname(os.path.abspath(__file__))
            print " Path is ", path
            return path
    return -1

def extractStub(targetFile):
    with open("targetFile", "r") as ins:
        for line in ins:
            if "<!--" in line:
                stubName = line.split()[1]
                print "Stub name is " + stubName
                return stubName
    return -1

