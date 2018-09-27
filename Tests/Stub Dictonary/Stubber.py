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

import string
import collections
import json
import os

global fileDictMD
global fileDictOther

fileDictMD = {}
fileDictOther= {}
global stubList
stubList = []

def createDict(pathTemp):

    #if the file path is not found in the dictionary continue
    if pathTemp not in fileDictMD.keys() or fileDictOther.keys():

        #if file path exists then continue
        if os.path.isfile(pathTemp):

                #if file is .md put in fileDictMD
                if pathTemp[pathTemp.index("."):] == ".md":

                    #get stub from pathTemp
                    pathTempRevrs = pathTemp[::-1]
                    stubTemp = pathTempRevrs[pathTempRevrs.index(".")+1:pathTempRevrs.index("-")]
                    stubTemp = stubTemp[::-1]

                    #store path/stub in dict and add to stubList
                    fileDictMD[pathTemp] = stubTemp
                    stubList.append(stubTemp)

                    #create json of sorted dict
                    fileDictJsonMD = json.dumps(collections.OrderedDict(sorted(fileDictMD.items())))

                    #open output file and write ordered dict then close file
                    output = open("Dictionary_output_md.txt", "w")
                    output.write(fileDictJsonMD)
                    output.close()

                else:
                    #if file is not .md put in fileDictOther
                    #get stub from pathTemp
                    stubTemp = pathTemp[pathTemp.index("-") + 1:pathTemp.index(".")]

                    # store path/stub in dict
                    fileDictOther[pathTemp] = stubTemp

                    # create json of sorted dict
                    fileDictJsonOther = json.dumps(collections.OrderedDict(sorted(fileDictOther.items())))

                    # open output file and write ordered dict then close file
                    output = open("Dictionary_output_other.txt", "w")
                    output.write(fileDictJsonOther)
                    output.close()


def getPath(stubTemp):

    pathTemp = ""

    #if stub is in dictMD continue
    if stubTemp in fileDictMD.values():

        #pathTemp is the file path associcated with the stub
        pathTemp = list(fileDictMD.keys())[list(fileDictMD.values()).index(stubTemp)]
        return pathTemp

    #if stub is in dictOther continue
    if stubTemp in fileDictOther.values():

        #pathTemp is the file path associcated with the stub
        pathTemp = list(fileDictOther.keys())[list(fileDictOther.values()).index(stubTemp)]
        return pathTemp

    return -1


def getStub(pathTemp):

    stubTemp = ""

    #if pathTemp is in dictMD continue
    if pathTemp in fileDictMD.keys():

        #stubTemp is the stub associcated with the path
        stubTemp = fileDictMD[pathTemp]
        return stubTemp

    #if pathTemp is in dictOther continue
    if pathTemp in fileDictOther.keys():

        #stubTemp is the stub associated with the path
        stubTemp = fileDictOther[pathTemp]
        return stubTemp

    return -1



def changePath(stubTemp, pathTemp):

    #if stub is in dict continute
    if stubTemp in fileDictMD.values():

        #delete the path/stub from dict
        del fileDictMD[list(fileDictMD.keys())[list(fileDictMD.values()).index(stubTemp)]]

        #store path/stub in dict
        fileDictMD[pathTemp] = stubTemp

        #create json of ordered dict
        fileDictJsonMD = json.dumps(collections.OrderedDict(sorted(fileDictMD.items())))

        #open output, write dict then close
        output = open("Dictionary_output_md.txt", "w")
        output.write(fileDictJsonMD)
        output.close()

    if stubTemp in fileDictOther.values():
        # delete the path/stub from dict
        del fileDictOther[list(fileDictOther.keys())[list(fileDictOther.values()).index(stubTemp)]]

        # store path/stub in dict
        fileDictOther[pathTemp] = stubTemp

        # create json of ordered dict
        fileDictJsonOther = json.dumps(collections.OrderedDict(sorted(fileDictOther.items())))

        # open output, write dict then close
        output = open("Dictionary_output_other.txt", "w")
        output.write(fileDictJsonOther)
        output.close()


def getStubList():
    return stubList
