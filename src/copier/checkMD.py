#----------------------------------------------------------------------
# Check Markdown File
# Author: Lukas Mallory
# Date: 09/12/2018
#
# Description: Takes a file and checks to see if it is a .md file. If so
# the file is converted to HTML and returned. If not the file is returned.
#---------------------------------------------------------------------

DEBUG = False

import shutil
import os
import src.converter.markdown2html as Converter

def LOG(string):
    if DEBUG:
        LOG(string)

def checkMDfile(fileName):
    if fileName.endswith('.md'):
        outputFile = Converter.markdown2html(fileName)
        return outputFile
    else:
        LOG(fileName)
        LOG('Not MD')
        return file
