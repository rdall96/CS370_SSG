#----------------------------------------------------------------------
# Check Markdown File
# Author: Lukas Mallory
# Date: 09/12/2018
#
# Description: Takes a file and checks to see if it is a .md file. If so
# the file is converted to HTML and returned. If not the file is returned.
#---------------------------------------------------------------------

import shutil
import os
import markdown2html as Converter

def checkMDfile(fileName , destDir, path):
    if fileName.endswith('.md'):
        outputFile = Converter.markdown2html(fileName)
        return outputFile
    else:
        print fileName
        print('Not MD')
        return file
