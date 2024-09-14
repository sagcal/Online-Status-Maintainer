# A Python script to keep your online status active on platforms like Teams, Skye, and Discord by simulating realistic mouse movements ensuring continuous activity without appearing robotic.


import pyautogui as screen
import random
import time

x, y = screen.size()
while True:
    x1 = random.randint(0, x)
    y1 = random.randint(0, y)
    screen.moveTo(x1, y1)
    screen.click(int(x/2)), (y-30)
    time.sleep(60)