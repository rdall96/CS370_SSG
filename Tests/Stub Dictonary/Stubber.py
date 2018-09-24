#Stub dictionary
#READ ME
#Pass store a file path and it will get the stub, enter it into the dict and write to the output file
#Pass getPath a stub and it will return the path associated with that stub
#Pass getStub a path and it will return the stub associated with that path
#Pass changePath a stub and a new path and it will update the dictionary
#The dictionary will be written to Dictionary_output.txt
#Derek Connelly 9/24/18

import string
import collections
import json

fileDict = {}


def createDict(pathTemp):

    #if the file path is not found in the dictionary continue
    if pathTemp not in fileDict.keys():

        #get stub from pathTemp
        stubTemp = pathTemp[pathTemp.index("-")+1:pathTemp.index(".")]

        #store path/stub in dict
        fileDict[pathTemp] = stubTemp

        #create json of sorted dict
        fileDictJson = json.dumps(collections.OrderedDict(sorted(fileDict.items())))

        #open output file and write ordered dict then close file
        output = open("Dictionary_output.txt", "w")
        output.write(fileDictJson)
        output.close()


def getPath(stubTemp):

    #Creates global 'Path Temp'
    global pathTemp

    #if stub is in dict continue
    if stubTemp in fileDict.values():

        #pathTemp is the file path associcated with the stub
        pathTemp = list(fileDict.keys())[list(fileDict.values()).index(stubTemp)]


def getStub(pathTemp):

    #creates global 'stubTemp'
    global stubTemp

    #if pathTemp is in dict continue
    if pathTemp in fileDict.keys():

        #stubTemp is the stub associcated with the path
        stubTemp = fileDict[pathTemp]


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
