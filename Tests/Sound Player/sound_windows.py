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
import winsound
from subprocess import Popen
p = Popen("play_sound.bat", cwd=r"C:\Users\derek\Desktop\Flock_SSG-master\Tests\Sound Player")
stdout, stderr = p.communicate()
