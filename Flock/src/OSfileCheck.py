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
import Stubber as Stub


def findFile(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def systemCheck():
    usrFileInput = raw_input("Enter the file name: ")
    # creating empty PathInput
    PathInput = ""
    usrPlatform = platform.system()
    if usrPlatform == "Linux":
        PathInput = "/home"
        fullFilePath = findFile(usrFileInput , PathInput)
#        print fullFilePath
    elif usrPlatform == "Windows":
        PathInput = "C:" + "\\"
        fullFilePath = findFile(usrFileInput , PathInput)
#        print fullFilePath
    elif usrPlatform == "Darwin":
        PathInput = "/Users/"
        fullFilePath = findFile(usrFileInput , PathInput)
#        print fullFilePath
    # added else check for not supported OSes
    # Ricky Dall'Armellina - 09/28/2018
    else:
        print("OS not supported")

    # FIXED: code would break when trying to check fo .isfile with NULL fullFilePath
    # Author: Ricky Dall'Armellina
    # Date: 09/28/2018
    # Wrapped check in try catch to prevent breaking
    try:
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

#-----------------------------------------------------------------------------------

systemCheck()
