

import os
import shutil
import checkMD as Checker


def fileCopy(srcDir, destDir):

    src_files = os.listdir(srcDir)
    for fileName in src_files:
        fullFileName = os.path.join(src, fileName)
        if (os.path.isfile(fileName)):
            Checker.checkMDfile(fileName)
            shutil.copy(fullFileName, destDir)

#-----------------------------------------------------------------------------
fileCopy('Markdown' , 'HTML')
