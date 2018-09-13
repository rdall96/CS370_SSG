#----------------------------------------------------------------------
# Directory File Cleaner
# Author: Lukas Mallory
# Date: 09/12/2018
#
# Description: Deletes all .html files from a given directory
# (can be modified to delete any file from a given directory)
#---------------------------------------------------------------------

import os

def directoryClean(srcDir):
   for root, dirs, files in os.walk(srcDir):
       for file in files:
           fullFilePath = os.path.join(root , file)
           if os.path.isfile(fullFilePath):
               if fullFilePath.endswith(".html"):
                   os.remove(os.path.join(root , file))