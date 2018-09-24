#----------------------------------------------------------------------
# Directory and File Copier
# Author: Lukas Mallory
# Date: 09/10/2018
#
# Description:Takes a source directory (Markdown) and copies its contents
# into a different directory (HTML) then converts all .md files within
# the HTML directory to .html files
#---------------------------------------------------------------------

from shutil import copytree, ignore_patterns
import errno
import shutil
import os
import markdown2html as Converter
import dirNaviV1 as Utils
from os.path import join, getsize

def copy(folderPath, destPath):
    try:
        shutil.copytree(folderPath, destPath ,  ignore=ignore_patterns('*.md'))

    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(folderPath, destPath)
        else:
            print('Directory not copied. Error: %s' % e)




#-------------------------------------------------------------------------------
copy('Markdown' , "HTML")

#create separate function def checkMDfile): if file.endswith('.md') call converter outputfile = converter.m2h(file) else do nothing return outputFile


#-------------------------------------------------------------------------------
