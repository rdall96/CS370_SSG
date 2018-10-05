#----------------------------------------------------------------------
# OScheckLooper
# Author: Lukas Mallory
# Date: 10/4/2018
#
# Description: Prompts user to enter folder name. Searchs from
# the computer's top directory down to find the folder. Once the
# folder is found it then creates the fullFolderPath based on the User's
# Operating System. It then uses the fullFolderPath to call the Stubber
# on a loop in order to grab the Stub of every file in the fullFolderPath.
#---------------------------------------------------------------------

import platform
import os
import Stubber as Stub


def findFile(name, path):
    for root, dirs, files in os.walk(path):
        if name in dirs:
            return os.path.join(root, name)

def systemCheck():
    usrDirInput = raw_input("Enter the folder name: ")
    # creating empty PathInput
    PathInput = ""
    usrPlatform = platform.system()
    if usrPlatform == "Linux":
        PathInput = "/home"
        fullFolderPath = findFile(usrDirInput , PathInput)
#        print fullFilePath
    elif usrPlatform == "Windows":
        PathInput = "C:" + "\\"
        fullFolderPath = findFile(usrDirInput , PathInput)
#        print fullFilePath
    elif usrPlatform == "Darwin":
        PathInput = "/Users/"
        fullFolderPath = findFile(usrDirInput , PathInput)
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
#        print fullFolderPath
        for root, dirs, files in os.walk(fullFolderPath):
            for file in files:
                fullFilePath = os.path.join(fullFolderPath, file)
                if os.path.isfile(fullFilePath):
#                    print fullFilePath
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
