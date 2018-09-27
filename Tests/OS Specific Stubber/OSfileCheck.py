#----------------------------------------------------------------------
# OSfileCheck
# Author: Lukas Mallory
# Date: 09/25/2018
#
# Description: Determines the user's operating system and checks to see
# if a given file exists.
#---------------------------------------------------------------------

import platform
import os
import getpass
import Stubber as Stub


def findFile(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def systemCheck():
    usrFileInput = raw_input("Enter the file name: ")
    usrPlatform = platform.system()
    usrName = getpass.getuser()
#    print usrName
    if usrPlatform == "Linux":
        PathInput = "/home/" + usrName
        fullFilePath = findFile(usrFileInput , PathInput)
#        print fullFilePath

    elif usrPlatform == "Windows":
        PathInput = "C:\\" + "Users\\" + usrName
        fullFilePath = findFile(usrFileInput , PathInput)
#        print fullFilePath

    elif usrPlatform == "Darwin":
        PathInput = "/Users/" + usrName
        fullFilePath = findFile(usrFileInput , PathInput)
#        print fullFilePath
    if os.path.isfile(fullFilePath):
        Stub.createDict(fullFilePath)
    else:
        print("ERROR!")
systemCheck()



#make a program to auto-rename files and put stubs in them
