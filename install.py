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

## NOTICE
# This is a minimalistic spin off the old script that can be found in /old/

__author__ = "Zackery Smith"
__email__ = "zackery.smith82307@gmail.com"
__copyright__ = "Copyright © 2021 Zackery Smith. All rights reserved."
__license__ = "GNU GPL-3.0"
__version_info__ = (0, 0, 1)
__version__ = ".".join(map(str, __version_info__))


##===-- Packages
from Bo_Boxes.bo_boxes import *
import os
import subprocess
import json
import time


##===-- Constants
__cwd__ = os.getcwd()
__home__ = os.path.expanduser("~")
__config__ = os.path.join(__home__, ".config")

logo = """
   ____  __________        _ __    __
  / __ \/ ____/ __ )__  __(_) /___/ /__  _____
 / / / / /   / __  / / / / / / __  / _ \/ ___/
/ /_/ / /___/ /_/ / /_/ / / / /_/ /  __/ /
\___\_\____/_____/\__,_/_/_/\__,_/\___/_/
"""


##===-- Timer
class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""
    pass


class Timer:
    def __init__(self):
        self._start_time = None


    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")
        self._start_time = time.perf_counter()


    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        return time.strftime('%H:%M:%S', time.gmtime(elapsed_time))


# Create cursor
cursor = Cursor(0, 0)

# Create timer (Used later)
timer = Timer()


##===-- QOL (Quality of Life) functions
def clean():
    """
    Cleans off the screen while keeping the logo displayed
    """
    os.system("clear")
    print(logo)


##===-- Installation functions
def _install_rob(rolling_release):
    if rolling_release == "stable":
        # Start timer
        timer.start()

        ##===-- I3 and I3-Gaps 
        print("QCBuilder will now start to install all required dependencies!")
        print("Checking for I3 installation")
        if "i3" in subprocess.getoutput("sudo apt list i3") or subprocess.getoutput("sudo apt list i3-wm"):
            pass
        else:
            print("Installing I3")
            os.system("sudo apt install i3 i3-wm i3status i3lock suckless-tools")
        
        print("Checking for I3-Gaps installation")
        if "i3-gaps" in subprocess.getoutput("sudo apt list i3-gaps"):
            pass
        else:
            print("Would you like to install i3-gaps (Recommended)?")
            selection = listBox(cursor, ["Yes", "No"])
            if selection == "Yes":
                os.system("sudo add-apt-repository ppa:regolith-linux/release")
                os.system("sudo apt update")
                os.system("sudo apt install i3-gaps")

        clean()
    
        ##===-- Font manager + Fonts
        print("Would you like to install fonts (HIGHLY recomended!)")
        selection = listBox(cursor, ["Yes", "No"])
        if selection == "Yes":
            print("Checking for font-manager")
            if "font-manager" in subprocess.getoutput("sudo apt list font-manager"):
                pass
            else:
                print("Would you like to install font-manager (REQUIRED)")
                selection = listBox(cursor, ["Yes", "No"])
                if selection == "Yes":
                    os.system("sudo apt install font-manager")
                else:
                    pass
            if "svn" in subprocess.getoutput("sudo apt list subversion"):
                pass
            else:
                os.system("sudo apt install subversion")

            print("Installing required fonts")
            os.system("mkdir rob-temp && cd rob-temp && svn checkout https://github.com/ZackeryRSmith/Rob/trunk/fonts/ && mv -v fonts/* . && rm -rf fonts/ && font-manager -i * && cd .. && rm -rf rob-temp")

        clean()
    
        ##===-- Install rob stable                                  
        # Make sure rob is deleted in current directory
        if os.path.exists(os.path.join(__cwd__, "Rob")):
            os.system(f'rm -rf {os.path.join(__cwd__, "Rob")}')
        os.system("git clone https://github.com/ZackeryRSmith/Rob/")

        ##===-- Check for rob install
        if os.path.exists(os.path.join(__config__, "i3", "scripts", "BI3L.sh")):
            print("It seems rob is already installed...")
            print("Checking for update")
            __rob_version__ = ""
            __git_rob_version__ = ""
            __git_repo__ = ""
            __git_author__ = ""
            __git_owner__ = ""
            # Get current installed version
            with open(f"{os.path.join(__config__, 'i3', 'info.json')}") as json_file:
                __rob_version__ = json.load(json_file)["version"]
            # Get most recent version
            with open(os.path.join(__cwd__, "Rob", "i3", "info.json")) as json_file:
                loaded_json = json.loads(json_file.read())
                __git_rob_version__ = loaded_json["version"]
                # get some more info while we are here    
                __git_repo__ = loaded_json["repo"]
                __git_author__ = loaded_json["author"]
                __git_owner__ = loaded_json["owner"]
                
            # If versions are the same quit
            if __rob_version__ == __git_rob_version__:
                elapsed_time = timer.stop()
                clean()
                print("Wohoo! Rob is up-to-date and ready to go! If you ever want to update again re-run this script.\n")
                print(f"""Additional Info on Installation
+----------------------------------------------------------+  
+-  Elapsed time: {elapsed_time}
+-  Github repository: {__git_repo__}
+-  Author: {__git_author__}
+-  Github repo owner: {__git_owner__} 
+-  Version: {__git_rob_version__}                     
+----------------------------------------------------------+""")
                exit()
        else:
            ##===-- Move around Robs components
            os.system(f"cd {os.path.join(__cwd__, 'Rob')} && mv i3 {__config__}")
            elapsed_time = timer.stop
            __git_repo__ = ""
            __git_author__ = ""
            __git_owner__ = ""
            __git_rob_version__ = ""
            # Get info
            with open(os.path.join(__cwd__, "Rob", "i3", "info.json")) as json_file:
                loaded_json = json.loads(json_file.read())
                __git_repo__ = loaded_json["repo"]
                __git_author__ = loaded_json["author"]
                __git_owner__ = loaded_json["owner"]
                __git_rob_version__ = loaded_json["version"]

            clean()
            print("Wohoo! Rob is installed and ready to go! If you ever want to update again re-run this script.\n")
            print(f"""Additional Info on Installation
 +----------------------------------------------------------+  
 +-  Elapsed time: {elapsed_time}
 +-  Github repository: {__git_repo__}
 +-  Author: {__git_author__}
 +-  Github repo owner: {__git_owner__} 
 +-  Version: {__git_rob_version__}                     
 +----------------------------------------------------------+""")
            exit()


    elif rolling_release == "bleeding_edge":
        print("There is no bleeding edge version of rob currently...")
    elif rolling_release == "nightly":
        print("There is no nightly version of rob currently...")

clean()
print("Checking wifi connectivity")
# Use pinging to see if there is a connection
try:
    ping_results = str(subprocess.check_output("ping -c 4 www.google.com", shell=True)).split("\\n")
except Exception as exc:
    # If you are here that means that you have no connection or an issue with ping arises
    print("Oops.. an issue has arrised when running `ping`. Try restarting your wireless/wired connection and trying again later!")
    exit()
if "unreachable" in ping_results:  # This
    print("Oops.. it seems you do not have a connection stable enough to run QCBuilder.. Please check your wireless/wired connection and try again later")
    exit()
clean()

# Check if QCBuilder is up-to-date (Add that code here)

saveSelection = False

# Check if user wants to save choices
print("Would you like to save chosen options after this point?")
selection = listBox(cursor, ["Yes", "No"])
if selection == "Yes":
    saveSelection = True

clean()

# Download desired version
print("What rolling release of Rob would you like to install")
selection = listBox(cursor, ["Stable (Recommended)", "Bleeding Edge", "Nightly"])

if selection == "Stable (Recommended)":
    _install_rob("stable")
elif selection == "Bleeding Edge":
    _install_rob("bleeding_edge")
elif selection == "Nightly":
    _install_rob("nightly")
