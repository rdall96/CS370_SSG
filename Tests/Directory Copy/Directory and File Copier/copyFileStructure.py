#----------------------------------------------------------------------
# Directory and File Copier
# Author: Lukas Mallory
# Date: 09/10/2018
#
# Description:Takes a source directory (Markdown) and copies its contents
# into a different directory (HTML) then converts all .md files within
# the HTML directory to .html files
#---------------------------------------------------------------------


import errno
import shutil
import os
import markdown2html as Converter

def copy(folderPath, destPath):
    src = folderPath
    dest = destPath
    try:
        shutil.copytree(src, dest)

    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)

    recursiveConversion(src, dest)

def recursiveConversion(src, dest):
    for root, dirs, files in os.walk(dest):
        for file in files:
            if file.endswith(".md"):
                #call converter here
                file = os.path.abspath(src + file)
                print(file)
                file = Converter.markdown2html(file)




#-------------------------------------------------------------------------------

copy('Markdown/', 'HTML/')
