#!/usr/bin/python
#----------------------------------------------------------------------
# Argument Checker for Flock
# Author: Ricky Dall'Armellina
# Date: 10/25/2018
#
# Description: Checks for argument flags when flock is called
#              from command line and calls respective component
#----------------------------------------------------------------------
DEBUG = False
def LOG(string):
    if DEBUG:
        print(string)
    return

import docs.showDocs as UsageDocs

# Argument flags
HELP_FLAG = "-help"
VERBOSE_FLAG = "-verbose"

def parse(argv):
    # check for command arguments and calls correct setting upon that
    # if argument count higher than 1 then there are argments
    if len(argv) > 1:
        # loop through all arguments and check their values
        for arg in argv:
            if arg == HELP_FLAG:
                LOG("-help called")
                UsageDocs.showDocs(1)
            elif arg == VERBOSE_FLAG:
                LOG("-verbose called")
                return True
            else:
                return False
    return