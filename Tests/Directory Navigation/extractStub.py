#!/usr/bin/python
#################################################
#    purpose: To extract the Stub for a given   #
#             markdown file                     #
#                                               #
#    Author: Dan Levy    Date:09/5/2018         #
#    Version: Initial                           #
#    Language: Python                           #
#################################################

import ~/Documents/GitHub/CS370_SSG/Tests/Directory\ Navigation/dirNaviV1.py

def extractStub(targetFile):
    with open("targetFile", "r") as ins:
        for line in ins:
            if "Stub" in line:
                stubName = line.split()[1]
                print "Stub name is " + stubName
                return stubName
    return -1
