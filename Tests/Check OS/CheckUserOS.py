#!/usr/bin/python
#----------------------------------------------------------------------
# Flock - Static Site Generator
# Author: Ricky Dall'Armellina
# Date: 09/28/2018
#
# Description: This program detects the user's OS and stores it for
#              future use. Getter fucntons to obtain the user OS and
#              home folder.
#----------------------------------------------------------------------

DEBUG = True

import platform, os

# Global Data

userOS = "" # OS for the user
homeDir = "" # user's home directory

# Other functions

def LOG(string):
    if DEBUG:
        print(string)

def detectOS():
    userOS = platform.system()
    if userOS == "Linux":
        homeDir = "/home/" + os.getlogin() + "/"
    elif userOS == "Windows":
        homeDir = "C:\\Users\\" + os.getlogin() + "\\"
    elif userOS == "Darwin":
        homeDir = "/Users/" + os.getlogin() + "/"
    LOG("User OS: " + userOS)
    LOG("User's home directory: " + homeDir)
    return

def getOS():
    return userOS

def getHomeDir():
    return homeDir

#----------------------------------------------------------------------
#----------------------------------------------------------------------

detectOS()