#!/usr/bin/python
#----------------------------------------------------------------------
# Static Site Generator
# Author: Ricky Dall'Armellina
# Date: 11/13/2018
#
# Description: Settings file for Flock
#----------------------------------------------------------------------

DEBUG = False
LOG_FILE = "log/"

def LOG(string):

    global DEBUG

    f = open(LOG_FILE, "a+")
    f.write("\n" + string)
    f.close()

    if DEBUG:
        print(string)
    
    return