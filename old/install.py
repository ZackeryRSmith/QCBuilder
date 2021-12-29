#!/usr/bin/env python
###########################################################################     
#                                                                         #     
#                    QCBuilder (Quick Config Builder)                     #     
#                         ~ The quickest config builder you've ever seen! #     
#                                                                         #     
#  Copyright (c) 2020, Zackery .R. Smith <zackery.smith82307@gmail.com>.  #     
#                                                                         #     
#  This program is free software: you can redistribute it and/or modify   #     
#  it under the terms of the GNU General Public License as published by   #     
#  the Free Software Foundation, either version 3 of the License, or      #     
#  (at your option) any later version.                                    #     
#                                                                         #     
#  This program is distributed in the hope that it will be useful,        #     
#  but WITHOUT ANY WARRANTY; without even the implied warranty of         #     
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #     
#  GNU General Public License for more details.                           #     
#                                                                         #     
#  You should have received a copy of the GNU General Public License      #     
#  along with this program. If not, see <http://www.gnu.org/licenses/>.   #     
#                                                                         #     
###########################################################################
    #                  ** Just a quick reminder **                    #
    #  This was created for ZackeryRSmith/Rob! All other configs wi-  ################################
    #  -ll not work (as of now). This was made for me when I need to  #    For more details visit    #
    #  setup my system configs without a huge hassle saving me a tr-  # github.com/ZackeryRSmith/Rob #
    #  -emendous amount of time.                                      ################################
    #                                                                 #
    ###################################################################


##===-- Packages
import os
import sys
import subprocess
import json
import re

##===-- Locations
locations = {
    "cwd":os.getcwd(),
    "~":os.path.expanduser("~"),
    ".config":str(os.path.expanduser("~"))+"/.config/",
    ".fonts":str(os.path.expanduser("~"))+"/.fonts/"
}

##===-- Important
qcbuilderSecrets = {
    "packageName":"QCBuilder",
    "version":"0.0.1"
}


##===-- ASCII colors
HEADER = '\033[95m'  # Dark pink + dark grey
BLACK = '\033[30m'  # Black
LIGHTBLACK = '\033[30;1m'  # Light black
GREEN = '\033[32m'  # Green
LIGHTGREEN = '\033[32;1m'  # Light green
CYAN = '\033[36m'  # Cyan
LIGHTCYAN = "\033[36;1m"  # Light cyan
RED = '\033[31m'  # Red
LIGHTRED = '\033[31;1m'  # Light red
BLUE = '\033[34m'  # Blue
LIGHTBLUE = '\033[34;1m'  # Light blue
MAGENTA = '\033[35m'  # Megenta
LIGHTMEGENTA = '\033[35;1m'  # Light megenta
YELLOW = '\033[33m'  # Yellow
LIGHTYELLOW = '\033[33;1m'  # Light yellow
WHITE = '\033[37m'  # White
LIGHTWHITE = '\033[37;1m'  # Light white
#OKBLUE = '\033[94m'  # Blue
#OKCYAN = '\033[96m'  # Light cyan
#OKGREEN = '\033[92m'  # Bright green
WARNING = '\033[93m'  # Yellow
CRITICAL = '\033[91m'  # Red
ENDC = '\033[0m'  # End color will remove all color formating
BOLD = '\033[1m'  # Bold text
UNDERLINE = '\033[4m'  # Underlined text ** Does not work with bolding

##===-- System controll class
class SystemControll:
    """
    :usage: Allows for the controll of the system like downloading, checking for files, and such.
    :libs: OS, Subprocess
    """
    def getSu():
        """
        :usage: Will pester the user for super user. ** Note that if install.py was ran as SU this function will not run.  
        :disclaimer: Not needed! Apt will bug the user for superuser for us.
        """
        pass

    def apt(operation, useSu, returnOutput, *args):
        """
        :usage: Allows for the use of the apt command.
        :param: return_output does just as it looks will return output, if false the return will change depending on operation passed
        """
        ## Reformat args to be usable
        args = str(args).replace("(", "").replace(")", "").replace("'", "").replace(",", " ")
        return subprocess.getoutput(str(str("sudo " if useSu == True else "") + "apt {} {}".format(operation, args)))

    def checkForDirs(dirList):
        pass

    def checkForFiles(fileList):
        pass

class Viewport:
    """
    :usage: Creates a terminal window to output debug info and to take inputs
    :libs: OS,
    """
    def __init__(self, display_types=True, color=True):
        self.display_types = display_types
        self.color = color

    def push(self, _type, *args):
        """
        :usage: Pushes any type of data to terminal. Result will vary depending on type of data being pushed.
        :param: _type, can be anything from text to image even commands, regardless the output will be rendered in the viewport
        :param: *args, all data being pushed.
        :note: Anything pushed will have an output on the viewport E.g. echo Hello will echo hello and such.
        """
        args = str(args).replace("(", "").replace(")", "").replace("'", "").replace(",", "")
        ## Why does python not have a switch case :I
        if _type == "header":
            # Text on header
            print(BOLD + str(args))
            # Divider
            print("--------------------------------" + ENDC)
        elif _type == "seperator":
            print(BOLD + "--------------------------------" + ENDC)
        elif _type == "plain-text":
            print(args)
        elif _type == "ascii-notification":
            print(BOLD + "[NOTIFICATION]  " + str(args) + ENDC)
        elif _type == "check":
            print(LIGHTCYAN + "[CHECK]  " + str(args) + ENDC)
        elif _type == "found":
            print(GREEN + "[FOUND]  " + str(args) + ENDC)
        elif _type == "not found":
            print(LIGHTRED + "[NOT FOUND]  " + str(args) + ENDC)
        elif _type == "installed":
            print(GREEN + "[INSTALLED]  " + str(args) + ENDC)
        elif _type == "skipping":
            print(BLUE + "[SKIPPING]  " + str(args) + ENDC)
        elif _type == "input":
            return input(LIGHTBLUE + "[INPUT]  " + str(args) + ENDC)
        elif _type == "warning":
            print(WARNING + "[WARNING]  " + str(args) + ENDC)
            return None
        elif _type == "critical":
            print(CRITICAL + "[CRITICAL]  " + str(args))
            exit()
        else:
            print(str("[{}] ".format(_type)) + str(args))
            return None        
 
### Now it gets real! ###
outputTerminal = Viewport()

####======---- Install functions (in a class for that fancy touch)
class InstallPackages:
    def installRob():
        # Make sure /tmp/zrstemp does not exists
        os.system("rm -rf /tmp/zrstemp/")
        # Clone ZackeryRSmith/Rob to /tmp/zrstemp/
        os.system("git clone https://github.com/ZackeryRSmith/Rob /tmp/zrstemp/")
        outputTerminal.push("installed", "Installed robs newest version files (/tmp/zrstemp/)")
        ## Move files to their respective position    
        # i3 configs
        if os.path.exists(os.path.join(locations[".config"], "i3")):
            outputTerminal.push("ascii-notification", "Wo, Wo, Wo. It seems Rob is already installed!")
            if "n" in outputTerminal.push("input", "Would you like to check for an update? [Y, n]"):
                outputTerminal.push("header", "Thank you for using Rob!")
                outputTerminal.push("plain-text", "If you want to check for an update and or install an update re-run this script! You could also turn on auto updating!")
            else:
                autoupdateRob = False
                if os.path.exists(os.path.join(locations["cwd"], "config.json")):  # If config file has not been created then this is the first run of config builder
                    pass
                else:
                    if "y" in outputTerminal.push("input", "Would you like to turn on auto updating (You will only be asked this once. To manully turn it on look towards github.com/ZackeryRSmith/QCBuilder/)? [y, N] "):
                        autoupdateRob = True                
                with open(os.path.join(locations["cwd"], "config.json"), "w+") as configFile:
                    configFile.write('{\n  "autoupdateRob":%s\n}' % (autoupdateRob))
            outputTerminal.push("header", "Thats it folks!")
            outputTerminal.push("plain-text", "I thank you for using Rob! If you think Rob looks just as good as I think it does give him a github star!")
        else:
            print("Now need to move i3 folder")

    def installI3():
        SystemControll.apt("install", True, False, "i3 i3-wm i3status i3lock suckless-tools")

    def installI3Gaps():
        os.system("sudo add-apt-repository ppa:regolith-linux/release")
        os.system("sudo apt update")
        os.system("sudo apt install i3-gaps")

    def installBumblebeeBar():
        SystemControll.apt("install", True, False, "python3-pip")
        os.system("pip install --user bumblebee-status")

    def installFonts(fonts):
        for font in fonts:
            fontPath = str(os.getcwd())+"fonts/"+font+".ttf"
            fontToInstall = font+".ttf"
            os.system("sudo font-manager -i %s" % (fontPath))

####======---- Misc functions
def getIndex(listInQuestion, whatToFind):
    """
    getIndex(), gets the index of a item in a list passed.
    :param: listInQuestion, the list to search trough.
    :param: whatToFind, is the item to search for in the listInQuestion
    """
    index = -1
    for item in listInQuestion:
        index+=1
        if item == whatToFind:
            return index


####======---- Basic checks

##===-- Wifi check
outputTerminal.push("check", "Checking for a wireless connection!")
WConnection = False  # False until proven otherwise.
# Use pinging to see if there is a connection
try:
    ping_results = str(subprocess.check_output("ping -c 4 www.google.com", shell=True)).split("\\n")
except Exception as exc:
    # If you are here that means that you have no connection or an issue with ping arises 
    outputTerminal.push("critical", 'An issue with "ping" has occured issue below\n'+exc)
## These ifs can be shorted by removing WConnection and combining this if and that else (this and that are labeled in comments).
try:
    if "4 received" in ping_results[7]:  # This
        WConnection = True
except:
    # If you are here that means that you have no connection
    outputTerminal.push("critical", "No wireless connection found!")

if WConnection == True:
    outputTerminal.push("found", "Wireless connection found!")
else: # that
    outputTerminal.push("critical", "Wireless connection not found! QCBuilder requires wifi to get packages from the internet!")
outputTerminal.push("header", "Check for crucial requirements")

##===-- Check for update
outputTerminal.push("check", "Checking for new update via git.")
# Check for update via github or config file if avalable
updateAvalable = False  # False until proven otherwise

##===-- Install config files from github if there is an update or there is no configs insi
if updateAvalable == True:
    # Get update via git.
    pass
else:
    outputTerminal.push("UP-TO-DATE", "You have the most up to date version of QCBuilder")

##===-- Check if I3 & I3-Gaps are installed (If not they will be installed.)
## I3 Check
outputTerminal.push("check", "Checking for an i3 installation.")
if "i3" in str(SystemControll.apt("list", True, True, "i3")) or str(SystemControll.apt("list", True, True, "i3-wm")):
    ## Alot of these are just for looks..
    outputTerminal.push("found", "Found an i3 installation.")
    outputTerminal.push("skipping", "Skipping i3 installation.")
else:
    # I3 is currently not installed
    outputTerminal.push("not found", "Could not find an i3 installation.")
    if "n" in outputTerminal.push("input", "Would you like to install i3? [Y,n] "):
        outputTerminal.push("critical", "Rob requires I3 to run closing setup.")  # critical is defined to auto close program when passed
    else:
        InstallPackages.installI3()

## I3-Gaps Check
outputTerminal.push("check", "Checking for i3-gaps installation.")
if "i3-gaps" in str(SystemControll.apt("list", True, True, "i3-gaps")):
    outputTerminal.push("found", "Found an i3-gaps installation")
    outputTerminal.push("skipping", "Skipping i3-gaps installation.")
else:
    if "n" in outputTerminal.push("input", "Would you like to install i3-gaps? [Y,n]"):
        outputTerminal.push("warning", "Rob was designed for i3-gaps, config will work just fine with i3 though!")
    else:
        # Install i3-gaps
        InstallPackages.installI3Gaps()

##==-- Check if a version of font-manager is present
skipFontInstalling = True  # True until set otherwise
outputTerminal.push("check", "Checking for font-manager")
if "font-manager" in str(SystemControll.apt("list", True, True, "font-manager")):
    outputTerminal.push("found", "Found a version of font-manager installed on your system")
    skipFontInstalling = False
else:
    outputTerminal.push("not found", "Unable to find a version of font-manager on your system!")
    if "n" in outputTerminal.push("input", "Would you like to install font-manager? [Y, n]"):
            if "n" in outputTerminal.push("input", "Are you sure you will (saying yes means QCBuilder will be unable to install fonts automaticly) [Y, n]"):
                SystemControll.apt("install", True, False, "font-manager")
                skipFontInstalling = False
    else:
        SystemControll.apt("install", True, False, "font-manager")
        skipFontInstalling = False

##==-- Check if required fonts are installed (If not they will be installed.)
outputTerminal.push("check", "Checking for fonts")

## Puts all required fonts that are not installed in a list for easy installation.  
requiredFonts = ["DejaVu Sans Mono for Powerline", "icomoon", "FontAwesome", "octicons", "Pomodoro", "Programming-Languages", "SFNS Display"]
installedRequiredFonts = []  # Placeholder
installedFonts = str(subprocess.check_output("font-manager -l", shell=True)).split("\\n")
# Append all installed fonts to installedRequiredFonts
for font in requiredFonts:
    if font in installedFonts:
        #installedRequiredFonts.append(requiredFonts[getIndex(requiredFonts, font)])
        installedRequiredFonts.append(requiredFonts[getIndex(requiredFonts, font)])
# Remove all fonts that are installed from requiredFonts
for font in installedRequiredFonts:
    requiredFonts.pop(getIndex(requiredFonts, font))

""" Redundent code (replaced by font-manger -l)
for index, font in enumerate(requiredFonts):
    # Method one
    if len(str(subprocess.getoutput("fc-list {}".format(font))).split("\n")) > 0:
        installedRequiredFonts.append(requiredFonts.pop(index))
    # Method two
    elif os.path.isfile(str(locations[".fonts"]+font)) == True:
        installedRequiredFonts.append(requiredFonts.pop(index))
    else:
        continue
"""

## Install all missing fonts
if len(requiredFonts) == 0:
    outputTerminal.push("found", "Found all required fonts!")
else:
    (outputTerminal.push("found", "Found {} required fonts: {}".format(len(installedRequiredFonts), installedRequiredFonts))) if len(requiredFonts) != 9 else None
    outputTerminal.push("not found", "Unable to find the following fonts: {}".format(requiredFonts))
    if "n" in outputTerminal.push("input", "Would you like to install the following fonts {}? [Y, n]".format(requiredFonts)):
        outputTerminal.push("warning", "Icons, Tool bars, and applications may look messed up if certain fonts are not installed. If you would like to manully install these fonts you can find a list of them at github.com/WillsCHEATTT/Rob/")
    else:
        InstallPackages.installFonts(requiredFonts)
    
outputTerminal.push("ascii-notification", "Done all checks & installs for important packages! Last step installing Rob's configs!")
outputTerminal.push("seperator")


## Install Rob
InstallPackages.installRob()
