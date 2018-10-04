#----------------------------------------------------------------------
# StubLooper
# Author: Lukas Mallory
# Date: 10/4/2018
#
# Description: Takes a folder path as input and calls the Stubber
# on a loop on every file in said folder path to grab the Stub. 
#---------------------------------------------------------------------

import os
import Stubber as Stub
import platform

def looper(folderPathInput):
        try:
            for root, dirs, files in os.walk(folderPathInput):
                for file in files:
                    fullFilePath = os.path.join(folderPathInput, file)
                    if os.path.isfile(fullFilePath):
                        Stub.createDict(fullFilePath)
                    else:
                        print("ERROR! Could not find file: " + usrFileInput)
        except TypeError as typeErr:
            print("File  " + usrFileInput + "  does not exist under any file path:  " + PathInput)
            #print(typeErr)
            print("If your directory is stored in an external drive, please move it under your OS drive")
        except ValueError as valErr:
            print("File  " + usrFileInput + "  does not exist under any file path:  " + PathInput)
            #print(valErr)
            print("If your directory is stored in an external drive, please move it under your OS drive")
        except:
            print("Unexpected error!")
        return



#IF PROGRAM DOES NOT WORK WITH OUTSIDE FILE PATH UNCOMMENT THE CODE BELOW
#AND RERUN THE PROGRAM INDEPENDENTLY

#def findFile(name, path):
#    for root, dirs, files in os.walk(path):
#        if name in dirs:
#            return os.path.join(root, name)
#
#def systemCheck():
#    usrFileInput = raw_input("Enter the dir name: ")
    # creating empty PathInput
#    PathInput = ""
#    usrPlatform = platform.system()
#    if usrPlatform == "Linux":
#        PathInput = "/home"
#        fullFilePath = findFile(usrFileInput , PathInput)
#        print fullFilePath
#        return fullFilePath
#
#fullFolderPath = systemCheck()
#looper(fullFolderPath)
