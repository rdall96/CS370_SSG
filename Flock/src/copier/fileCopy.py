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

# Ricky Dall'Armellina
# 10/02/2018
# Adding delete .md files from selcted folder
def deleteMD(folder):
    LOG("Selected directory: " + folder)
    # loop through files and directories and remove markdown files from it
    for root, dirs, files in os.walk(folder):
        for fileName in files:
            if fileName.endswith(".md"):
                try:
                    LOG("Removing markdown file directory")
                    os.remove(os.path.join(root, fileName))
                except:
                    print("An error occured while removing markdown files")
                    return False
    return True