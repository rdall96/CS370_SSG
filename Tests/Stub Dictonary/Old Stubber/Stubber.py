#Stub generator and dictionary
#READ ME
#Pass stubGen a file path to generate a stub, write it to the file, and add it to the dict
#Pass stubCheck a file path and stub to check if they match, if not, delete that line from dict
#and add the new file path and stub to the dict
#The dictionary will be written to Dictionary_output.txt
#Derek Connelly 9/4/18


import random
import string
import collections
import json

fileDict = {}


def stubGen(pathTemp):
    if pathTemp not in fileDict.keys():
        stubTemp = ""
        for x in range(4):
            temp = random.randint(0, 1)
            if temp == 1:
                stubTemp = stubTemp + str(random.randint(0, 9))
            else:
                stubTemp = stubTemp + random.choice(string.ascii_letters)
        if stubTemp in fileDict.values():
            goto(20)
        fileDict[pathTemp] = stubTemp
        fileDictJson= json.dumps(collections.OrderedDict(sorted(fileDict.items())))
        output = open("Dictionary_output.txt", "w")
        output.write(fileDictJson)
        output.close()
        line = '<!-- ' + stubTemp + '-->\n'
        f = open(pathTemp, "r+")
        file_data = f.read()
        f.seek(0,0)
        f.write(line.rstrip('\r\n') + '\n' + file_data)
        f.close()


def stubCheck(pathTemp, stubTemp):
        if stubTemp in fileDict.values() and (list(fileDict.keys())[list(fileDict.values()).index(stubTemp)] != pathTemp):
            del fileDict[list(fileDict.keys())[list(fileDict.values()).index(stubTemp)]]
            fileDict[pathTemp] = stubTemp
            fileDictJson = json.dumps(collections.OrderedDict(sorted(fileDict.items())))
            output = open("Dictionary_output.txt", "w")
            output.write(fileDictJson)
            output.close()


def loadDict(nfile):
    with open(nfile, 'r') as inf:
        fileDict = eval(inf.read())
    fileDictJson = json.dumps(collections.OrderedDict(sorted(fileDict.items())))
    output = open("Dictionary_output.txt", "w")
    output.write(fileDictJson)
    output.close()


def goto(line):
    global lineNumber
    line = lineNumber
