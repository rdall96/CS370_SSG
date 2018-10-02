#----------------------------------------------------------------------
# Directory File Copy
# Author: Lukas Mallory
# Date: 09/12/2018
#
# Description: Copies files from a target directory
# to a destination directory. Calls checkMD before copying.
#---------------------------------------------------------------------

DEBUG = False

import os, shutil

def LOG(string):
    if DEBUG:
        LOG(string)

def fileCopy(srcDir, destDir):
    for root, dirs, files in os.walk(srcDir):
        for file in files:
            fullFilePath = os.path.join(root , file)
            if os.path.isfile(fullFilePath):
                LOG(fullFilePath + "  1")
                path = os.path.dirname(fullFilePath)
                path = path.replace("Markdown" , '')
    shutil.copytree(srcDir, destDir)
    return True
