#!/usr/bin/python
#################################################
#    purpose: To explore recursive directory    #
#             navigation in python              #
#                                               #
#    Author: Dan Levy    Date:09/3/2018         #
#    Version: Second                            #
#    Langauge: Python                           #
#################################################

DEBUG = False
def LOG(string):
    if DEBUG:
        print(string)
    return
def enableDEBUG(isEnable):
    global DEBUG
    if isEnable:
        DEBUG = True
    else:
        DEBUG = False
    return

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
            LOG(targetDir + " found")
            path = os.path.join(root, targetDir)
            LOG(" Path is " + path)
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
            LOG(targetFile + " found")
            path = os.path.join(root, targetFile)
            LOG(" Path is " + path)
            return path
    return -1


