#----------------------------------------------------------------------
# Check Markdown File
# Author: Lukas Mallory
# Date: 09/12/2018
#
# Description: Takes a file and checks to see if it is a .md file. If so
# the file is converted to HTML and returned. If not the file is returned.
#---------------------------------------------------------------------
import os
import markdown2html as Converter

def checkMDfile(file):
    if file.endswith('.md')
        outputFile = Converter.markdown2html(fileName)
        return outputFile
    else:
        print('Not MD')
        return file
