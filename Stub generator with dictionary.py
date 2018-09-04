#Stub generator and dictionary
#READ ME
#Enter a 1 to add a new file path, stub will be generated then an ordered list of all file paths and their stubs will be created
#Enter a 2 to change a file path, enter the stub then enter the new file path
#Enter a 3 to end the program
#Derek Connelly 9/4/18

import random
import string
import collections

cond = 0
fileDict = {}
while cond != 3:
    cond = input("Enter a number\n 1:New Path\n 2.Edit Path\n 3.Exit\n")
    cond = int(cond)
    if cond == 1:
        stubTemp = ""
        pathTemp = input("Enter the file path\n")
        for x in range(4):
            temp = random.randint(0, 1)
            if temp == 1:
                stubTemp = stubTemp + str(random.randint(0, 9))
            else:
                stubTemp = stubTemp + random.choice(string.ascii_uppercase)
        fileDict[pathTemp] = stubTemp
        print(collections.OrderedDict(sorted(fileDict.items())))
    elif cond == 2:
        stubTemp = input("Enter a stub to change the path\n")
        if stubTemp in fileDict.values():
            del fileDict[list(fileDict.keys())[list(fileDict.values()).index(stubTemp)]]
            pathTemp = input("Enter the new path name\n")
            fileDict[pathTemp] = stubTemp
            print(collections.OrderedDict(sorted(fileDict.items())))
        else:
            print("That stub does not exist\n")



