#----------------------------------------------------------------------
# Sound Byte Player
# Author: Lukas Mallory
# Date: 10/30/2018
#
# Description: Plays a sound byte of birds chirping at a specific time
# (When the website is done creating)
#---------------------------------------------------------------------

import os

#When website is finished generating do this
#NOTE: replace file path with file path that contains sound file
os.popen2("cvlc /home/lukeylad/Documents/Test/Canary.mp3 --play-and-exit")
