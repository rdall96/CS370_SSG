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

def copy():
    src = 'Markdown/'
    dest = 'HTML'
    try:
        shutil.copytree(src, dest)

    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)

        recursiveConversion(dest)

copy()

def recursiveConversion(dest):
    for root, dirs, files in os.walk(dest):
        for file in files:
            if file.endswith(".md"):
                #call converter here
