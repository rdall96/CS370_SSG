#-------------------------------------------------------------------------
# Test for Stubber
# Ricky Dall'Armellina
# 10/02/2018
#-------------------------------------------------------------------------

DEBUG = True

import os, shutil
import Stubber2 as Stubber

# Test variables
MARKDOWN_FOLDER = "Markdown-test"
TEST_STUB = "main"
TEST_PATH = "/Volumes/Ricky/CS 370/Stubber/Markdown-test/assets/subscribe-gif.gif"


def LOG(string):
    if DEBUG:
        print(string)
    return

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

print("\n - Stubber Test - \n")

# folder with markdown test files
mFolder = os.path.abspath(MARKDOWN_FOLDER)
#LOG("Folder absolute path: " + mFolder)

#populate dictonary test
LOG("\nPopulating dictonary with files from: " + mFolder)
Stubber.populateDict(mFolder)

#get path from stub test
LOG("\nRequesting path for " + TEST_STUB)
testPath = Stubber.getPath(TEST_STUB)
LOG("   Test path: " + testPath)

#get stub from path test
LOG("\nRequesting stub for " + TEST_PATH)
testStub = Stubber.getStub(TEST_PATH)
LOG("   Test stub: " + testStub)

#get stub list test
LOG("\nRequesting stub list")
testList = Stubber.getStubList()
LOG("   Stub list: " + (str)(testList))

print("\nDONE!\n")
