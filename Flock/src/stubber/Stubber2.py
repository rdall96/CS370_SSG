#Stub dictionary
#READ ME
#IMPORTANT: STUB SYNTAX "'FILEPATH'-'STUB'.'FILE TYPE'"
#EX: C:\Users\Derek\Desktop\Test-1234.txt stub=1234
#Pass store a file path and it will get the stub, enter it into the dict and write to the output file
#Pass getPath a stub and it will return the path associated with that stub
#Pass getStub a path and it will return the stub associated with that path
#Pass changePath a stub and a new path and it will update the dictionary
#The dictionary will be written to Dictionary_output.txt
#Derek Connelly 9/24/18

#------------------------------------------------------------------
# Stubber2.py
# Ricky Dall'Armellina
# ver: 2.0
# Revision made to fix bugs with ver1.0 and improve execution flow
# 10/03/2018
# Changes marked with comment 'v2.0' were made in this revision
# NOTE: paths are 'keys' in the dictonary, while stubs are 'values'
#------------------------------------------------------------------

from .. import settings
import string
import collections
import json
import os
import ast
import re
# v2.0 - Removed imports and calls to os.chmod()

global fileDict

# v2.0 - Changed file links to global variable. Easier to move the files in the future
dictonaryOutFile = settings.DICTIONARY_FILE
fileDict = {}
# v2.0 - Removed second dictonary
global stubList
stubList = []

# v2.0 - Renamed to addToDict(), which makes more sense given the purpose of the function
def addToDict(pathTemp):
    # check if path ands with ".md" and if so replace with ".html"
    if pathTemp.endswith(".md"):
        pathTemp = pathTemp[:-3] + ".html"
    #if the file path is not found in the dictionary continue
    if pathTemp not in fileDict.keys():
        # v2.0 - Removed check if file exists. FIle is valid since it's fed by populateDict() which parses through files only
        settings.LOG("Adding new file to dictonary  -  " + pathTemp)
        # v2.0 - Removed check if file is md, all files go in a single dictonar
        #get stub from pathTemp
        pathTempRevrs = pathTemp[::-1]
        stubTemp = pathTempRevrs[pathTempRevrs.index(".")+1:pathTempRevrs.index("-")]
        stubTemp = stubTemp[::-1]
        #store path/stub in dict and add to stubList
        fileDict[pathTemp] = stubTemp
        stubList.append(stubTemp)
        #create json of sorted dict
        fileDictJsonMD = json.dumps(collections.OrderedDict(sorted(fileDict.items())))
        #open output file and write ordered dict then close file
        # v2.0 - Changed call to file open with global varible for the file
        output = open(dictonaryOutFile, "w")
        output.write(fileDictJsonMD)
        output.close()
        return True
    # v2.0 - Removed second dictonary check
    else:
        settings.LOG("File already in dictionary")
        return False
    return


def populateDict(folder):
    # v2.0 - Adder counter for number of files passed to addToDict(). No actual purpose besides visually seeing how many files went through
    filesStubbed = 0
    for root, dirs, files in os.walk(folder):
        for fileName in files:
            #Go to next file in loop if it is a hidden file
            if(re.search("^\.", fileName, flags = 0)):
                continue
            # v2.0 - Renamed function call according to changes
            filePath = os.path.join(root, fileName)
            # remove top fiolder from file path for correct linking
            filePath = re.sub((folder + "/"), "", filePath)
            addToDict(filePath)
            filesStubbed += 1
    settings.LOG("\nStubbed " + (str)(filesStubbed) + " files\n")
    # v2.0 - Returning number of files stubbed. Maybe useful to print back to the user?
    return filesStubbed


def getPath(stubTemp):
    # v2.0 - Added settings.LOG() throught the function to test outputs
    pathTemp = ""
    #if stub is in dictonary continue
    if stubTemp in fileDict.values():
        settings.LOG("Selected stub is in dictonary")
        #pathTemp is the file path associcated with the stub
        pathTemp = list(fileDict.keys())[list(fileDict.values()).index(stubTemp)]
        settings.LOG("   Path: " + pathTemp)
        return pathTemp
    # v2.0 - Removed getPath() from second dictonary
    else:
        settings.LOG("Stub '" + stubTemp + "' NOT in dictionary.")
    return -1


def getStub(pathTemp):
    # v2.0 - Added settings.LOG() throught the function to test outputs
    stubTemp = ""
    #if pathTemp is in dictionary continue
    if pathTemp in fileDict.keys():
        settings.LOG("Selected path is in dictonary")
        #stubTemp is the stub associcated with the path
        stubTemp = fileDict[pathTemp]
        settings.LOG("   Stub: " + stubTemp)
        return stubTemp
    # v2.0 - Removed getStub() from second dictionary
    else:
        settings.LOG("Path '" + pathTemp + "' NOT in dictionary.")
    return -1


def changePath(stubTemp, pathTemp):

    #if stub is in dict continute
    if stubTemp in fileDict.values():

        #delete the path/stub from dict
        del fileDict[list(fileDict.keys())[list(fileDict.values()).index(stubTemp)]]

        #store path/stub in dict
        fileDict[pathTemp] = stubTemp

        #create json of ordered dict
        fileDictJson = json.dumps(collections.OrderedDict(sorted(fileDict.items())))

        #open output, write dict then close
        output = open("Dictionary_output.txt", "w")
        output.write(fileDictJson)
        output.close()


def getStubList():
    settings.LOG("\n" + (str)(stubList) + "\n")
    return stubList

def loadDict(nfile):
    #pass the path of a txt file that a dictionary was written to
    #and fileDict will become that dictionary
    global fileDict
    with open(nfile, 'r') as f:
        s = f.read()
        fileDict = ast.literal_eval(s)
    fileDictJson = json.dumps(collections.OrderedDict(sorted(fileDict.items())))
    output = open("Dictionary_output.txt", "w")
    output.write(fileDictJson)
    output.close()
    settings.LOG(fileDict)

