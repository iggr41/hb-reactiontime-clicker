# -*- coding: UTF-8 -*-
import pyautogui

color = (75, 219, 106)
greenR = color[0]
greenG = color[1]
greenB = color[2]
x, y = pyautogui.position()
timer = 0

while pyautogui.pixel(x, y) != color:
    while timer < 5:
        x, y = pyautogui.position()
        if pyautogui.pixel(x, y) == color:
            pyautogui.click(x, y)
            print("Click %d" % (timer + 1))
            pyautogui.click(x, y)
            timer += 1







