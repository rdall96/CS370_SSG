#!/usr/bin/python
#----------------------------------------------------------------------
# Theme Selector
# Author: Ricky Dall'Armellina
# Date: 10/226/2018
#
# Description: Theme picker for Flock.
#----------------------------------------------------------------------
DEBUG = False
def LOG(string):
    if DEBUG:
        print(string)
    return

import shutil

FLOCK_ICON_PATH = "Themes/flock_icon.png"
THEME_FOLDER = "Themes/"
THEME_NAMES = """
 1. Light theme
 2. Dark theme
 3. Fun theme
 4. Blue Accent
 5. Firebrick Accent
 6. Green Accent
 7. Orange Accent
 8. Purple Accent
 9. Select your own
"""

def selectTheme(destinationFolder, verbose):

    THEME_VALID = False

    # get verbose mode
    if verbose:
        DEBUG = True
    
    # ask user to pick a theme
    # also keeps asking in case the input isn't valid
    while not THEME_VALID:
        print("Available themes" + THEME_NAMES)
        themeOption = input("Choose a theme: ")
        if themeOption == '1':
            # light theme
            LOG("Light theme choosen")
            theme = "light_theme"
            themePath = THEME_FOLDER + theme + ".css"
            THEME_VALID = True
        elif themeOption == '2':
            # dark theme
            LOG("Dark theme choosen")
            theme = "dark_theme"
            themePath = THEME_FOLDER + theme + ".css"
            THEME_VALID = True
        elif themeOption == '3':
            # colored theme
            LOG("Fun theme choosen")
            theme = "fun_theme"
            themePath = THEME_FOLDER + theme + ".css"
            THEME_VALID = True
        elif themeOption == '4':
            # blue theme
            LOG("Blue Accent theme selected")
            theme = "std_blue"
            themePath = THEME_FOLDER + theme + ".css"
            THEME_VALID = True
        elif themeOption =='5':
            # firebrick theme
            LOG("Firebrick Accent theme selected")
            theme = "std_firebrick"
            themePath = THEME_FOLDER + theme + ".css"
            THEME_VALID = True
        elif themeOption == '6':
            # green theme
            LOG("Green Accent theme selected")
            theme = "std_green"
            themePath = THEME_FOLDER + theme + ".css"
            THEME_VALID = True
        elif themeOption == '7':
            # orange theme
            LOG("Orange Accent theme selected")
            theme = "std_orange"
            themePath = THEME_FOLDER + theme + ".css"
            THEME_VALID = True
        elif themeOption == '8':
            # purple theme
            LOG("Purple Accent theme selected")
            theme = "std_purple"
            themePath = THEME_FOLDER + theme + ".css"
            THEME_VALID = True
        elif themeOption == '9':
            #custom user theme selected
            LOG("Custom user theme selected")
            themePath = input("Insert the path and name to your custom theme: ")
            THEME_VALID = True
        else:
            LOG("The selected theme does not exist")
            print("\nPlease choose a valid theme")
        
    # copy stylesheet
    shutil.copy2(themePath, (destinationFolder + "/styles.css"))
    # copy Flock icon
    shutil.copy2(FLOCK_ICON_PATH, (destinationFolder + "/flock_icon.png"))
    
    return