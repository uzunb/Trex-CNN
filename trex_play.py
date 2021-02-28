#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 22:32:38 2021

@author: buzun
"""

from keras.models import model_from_json
import numpy as np
from PIL import Image
import keyboard
import time
from mss import mss


# game map
limits = {"top":375, "left": 740, "width":250, "height": 100 }
sct = mss()

# img size
width = 250
height = 100


# model yükle
model = model_from_json(open("/home/buzun/Workspace/Trex-CNN/model.json","r").read())
model.load_weights("trex_weight.h5")



# down = 0, right = 1, up = 2
labels = ["Down", "Right", "Up"]

frameRateTime = time.time()
counter = 0
i = 0
delay = 0.32
key_down_pressed = False

keyboard.press(keyboard.KEY_UP)
keyboard.release(keyboard.KEY_UP)

while True:
    
    img = sct.grab(limits)
    img1 = Image.frombytes("RGB", img.size, img.rgb)
    img2 = np.array(img1.convert("L").resize((width, height))) / 255
    
    X = np.array([img2])
    X = X.reshape(X.shape[0], width, height, 1)
    
    results =  model.predict(X)
    result = np.argmax(results)
    
    print("---------------------")
    # print("Down: {} \nRight:{} \nUp: {} \n".format(results[0][0]
    #                                                    ,results[0][1]
    #                                                    ,results[0][2]))
    print("action : ", result, "\n frame : ", i)

    # down = 0
    if result == 0:
                    
        keyboard.press(keyboard.KEY_DOWN)
        key_down_pressed = True
        
     # up = 2
    elif result == 2:
        
        if key_down_pressed:
            keyboard.release(keyboard.KEY_DOWN)
        time.sleep(delay)
        keyboard.press(keyboard.KEY_UP)
        keyboard.release(keyboard.KEY_UP)
        print("pressed up\n")
        
        if i < 1500:
            time.sleep(0.3)
        elif 1500 < i and i < 5000:
            time.sleep(0.2)
        else:
            time.sleep(0.17)

        #keyboard.press(keyboard.KEY_DOWN)
        #keyboard.release(keyboard.KEY_DOWN)


    counter += 1
    
    if (time.time() - frameRateTime) > 1:
        
        counter = 0
        frameRateTime = time.time()
        if i <= 1500:
            delay -= 0.003
        else:
            delay -= 0.005
        if delay < 0:
            delay = 0
        

        i += 1


























