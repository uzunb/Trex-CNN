#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 01:38:22 2021

@author: buzun
"""
import keyboard
import uuid
import time
from PIL import Image
from mss import mss

"""
http://www.trex-game.skipser.com/
"""

# game map
limits = {"top":375, "left": 740, "width":250, "height": 100 }

# mss is cuts region of interest frame
sct = mss()

i = 0

def recordScreen(recordID, key):
    global i
    
    i += 1
    print("{}: {}".format(key, i))
    
    img = sct.grab(limits)
    im = Image.frombytes("RGB", img.size, img.rgb)
    im.save("./img/{}_{}_{}.png".format(key, recordID, i)) 

isExit = False

def exit():
    global isExit
    isExit = True

keyboard.add_hotkey("esc", exit)

recordID = uuid.uuid4()

while True:
    
    if isExit: break

    try:
        if keyboard.is_pressed(keyboard.KEY_UP):
            recordScreen(recordID, "up")
            time.sleep(0.1)
        elif keyboard.is_pressed(keyboard.KEY_DOWN):
            recordScreen(recordID, "down")
            time.sleep(0.1)
        elif keyboard.is_pressed("right"):
            recordScreen(recordID, "right")
            time.sleep(0.1)
    except RuntimeError: continue

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
