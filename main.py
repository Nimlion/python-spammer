import pyautogui
import time

time.sleep(5)
f = open("textfile", "r")

for sentence in f:
    pyautogui.typewrite(sentence)
    pyautogui.press("enter")

f.close()
