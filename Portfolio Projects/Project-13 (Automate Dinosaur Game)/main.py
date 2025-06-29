import numpy as np
import time

import pyautogui
from PIL import ImageGrab
from fontTools.subset import intersect
from PIL import *
from fontTools.ttLib.woff2 import bboxFormat

#
# pyautogui.moveTo(500,50,3)
# pyautogui.click(interval=3)
# pyautogui.click()

# pyautogui.typewrite("google.com", interval=1)
# pyautogui.keyDown('delete')
# pyautogui.keyDown('Enter')

# coordinates

# def openChrome():
# pyautogui.press('win')
# pyautogui.typewrite('chrome',interval=0.1)
# pyautogui.press('enter',interval=0.1)
# pyautogui.sleep(2)
# pyautogui.press('tab',presses=1,interval=0.1)
# pyautogui.press('enter',interval=0.1)
# pyautogui.hotkey('ctrl','t')
# pyautogui.typewrite('chrome://dino/')
# pyautogui.press('enter')


box = (755, 250, 780, 280)
# img = ImageGrab.grab(bbox=box)
# img.show()

def detect_obstacle():
    # box = (720, 430, 860, 470)
    box = (800, 240, 860, 290)
    img = ImageGrab.grab(bbox=box).convert('L')
    img_np = np.array(img)
    light_pixels = np.sum(img_np > 100)
    print("Light pixels:", light_pixels)
    return light_pixels > 50  # You may lower to 30 if cactus is missed

def auto_dino():
    print("Bot running...")
    while True:
        if detect_obstacle():
            pyautogui.press('space')
            print("Jump!")
            time.sleep(0.05)





if __name__ == "__main__":
    time.sleep(2)  # Time to switch to desktop
    pyautogui.hotkey('win','d',interval=0.5)
    pyautogui.press('win',interval=0.2)
    pyautogui.typewrite('chrome', interval=0.1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('tab',presses=8,interval=0.1)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite('chrome://dino/', interval=0.1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('space')
    # Start the game
    time.sleep(1)
    auto_dino()



# pyautogui.hotkey('alt','tab',interval=0.1)
# captimg = ImageGrab.grab((720, 250, 780, 280))
# captimg.show()