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

from . import settings
import platform
import os
import Flock.src.stubber.Stubber2 as Stub


def findFile(name, path):
    # Added usrFolder to store path
    # Ricky Dall'Armellina
    # 10/07/2018
    usrFolder = "" # to be used in try catch
    # Wrapped in try catch to prevent code from breaking when looking for an unexisting folder path
    # Ricky Dall'Armellina
    # 10/07/2018
    try:
        for root, dirs, files in os.walk(path):
            if name in dirs:
                usrFolder = os.path.join(root, name)
                return usrFolder
    except TypeError as typeErr:
        settings.LOG("Folder  " + usrFolder + "  does not exist under any path:  " + path)
        settings.LOG(typeErr)
        settings.LOG("If your directory is stored in an external drive, please move it under your OS drive")
    except ValueError as valErr:
        settings.LOG("Folder  " + usrFolder + "  does not exist under any path:  " + path)
        settings.LOG(valErr)
        settings.LOG("If your directory is stored in an external drive, please move it under your OS drive")
    except:
        settings.LOG("Unexpected error!")
    return


def systemCheck(usrDirInput):
    # removed user request and made input a function argument
    # Ricky Dall'Armellina
    # 10/07/2018
    PathInput = "" # creating empty PathInput
    usrPlatform = platform.system()
    if usrPlatform == "Linux":
        PathInput = "/home"
        fullFolderPath = findFile(usrDirInput , PathInput)
    elif usrPlatform == "Windows":
        PathInput = "C:" + "\\"
        fullFolderPath = findFile(usrDirInput , PathInput)
    elif usrPlatform == "Darwin":
        PathInput = "/Users/"
        fullFolderPath = findFile(usrDirInput , PathInput)
    # added else check for not supported OSes
    # Ricky Dall'Armellina - 09/28/2018
    else:
        print("\nOS not supported\n")
    return fullFolderPath
