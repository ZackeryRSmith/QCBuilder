#!/usr/bin/env python
# Terminal like thing with python

##===-- Imports
import os
import subprocess

# Requires terminator terminal for the extra configurations!
class terminal:
    def __init__(self, title, width, height, position="+240+125",show=True):                                 
        self.title = title                                                                                
        self.width = width                          
        self.position = position
        self.height = height                                                                                      
        self.show = show                                                            
                                                                                                              
    def push(self, _type, *args):
        args = str(args).replace("(", "").replace(")", "").replace("'", "").replace(",", "")
        ## Why does python not have a switch case :I
        if _type == "plain-text":
            print(args)
        elif _type == "input":
            return input("[INPUT]  " + str(args))
        elif _type == "warning":
            print("[WARNING]  " + str(args))
            return None
        elif _type == "critical":
            print("[CRITICAL]  " + str(args))
            return None
        else:
            print(str("[{}] ".format(_type)) + str(args))
            return None        

    def start(title, geometry):
        #terminator -x sh -c '/home/test/test.sh; read -p "Press any key... " -n1'
        #os.system("terminator --geometry {} -T {} -e python3 ./src/terminpy.py".format(geometry, title))
        os.system(str("terminator --geometry 400x800 -T Test -x sh -c " + '"python3 /src/terminpy.py"'))
        quit()

input("test")
#terminator --geometry 1200x800+240+125 -T "" -e "python3"
