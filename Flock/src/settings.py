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
IS_MODULE = True # toggle to execute FLock locally or installed as a module, useful for testing FRIST_USE_FILE path

def LOG(string):

    global DEBUG

    f = open(LOG_FILE, "a+")
    f.write("\n" + string)
    f.close()

    if DEBUG:
        print(string)
    
    return

def runAsLocal(isLocal):

    global IS_MODULE

    if isLocal:
        IS_MODULE = False
        LOG("Flock is executing locally.")
    else:
        IS_MODULE = True
        LOG("Flock is executing as an installed module.")
    
    return
