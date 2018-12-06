#!/usr/bin/python
#################################################
#    purpose: To explore recursive directory    #
#             navigation in python              #
#                                               #
#    Author: Dan Levy    Date:09/3/2018         #
#    Version: Second                            #
#    Langauge: Python                           #
#################################################

from .. import settings
import os
from os.path import join, getsize
from shutil import copyfile
import shutil


#Variables: targetDir is the directory to find
#           topDirectory is the directory you want to search all the children of
#Return Value(s): returns the absolute path of the target Directory, or -1 on failure
#Usage: targetDir must be passed in as a string containing the directory name
#       topDirectory msut be passed in as a string of the absolute path of the directory
def findTargetDir(targetDir, topDirectory):
    for root, dirs, files in os.walk(topDirectory):
        if targetDir in dirs:
            settings.LOG(targetDir + " found")
            path = os.path.join(root, targetDir)
            settings.LOG(" Path is " + path)
            return path
    return -1

#Variables: targetFilePath is absolute file path you want moved
#           newFilePath is the absolute file path of the target file's new locatione
#Usage: Both arguments must be passed in as strings of the absolute file path
def transcriptTargetFile(targetFilePath, newFilePath):
    shutil.move(targetFilePath, newFilePath)

#Variables: targetFile is the file to find
#           topDirectory is the directory you want to search all the children of
#Return Value(s): returns the absolute path of the target file, or -1 on failure
#Usage: targetFile must be passed in as a string containing the file name
#       topDirectory must be passed in as a string of the absolute path of the directory
def findTargetFile(targetFile, topDirectory):
    for root, dirs, files in os.walk(topDirectory):
        if targetFile in files:
            settings.LOG(targetFile + " found")
            path = os.path.join(root, targetFile)
            settings.LOG(" Path is " + path)
            return path
    return -1


