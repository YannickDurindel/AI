import pyautogui
import time
import pyperclip
import pyttsx3

pyautogui.moveTo(0,766)
time.sleep(1)

pyautogui.moveTo(500, 420)
time.sleep(1)
pyautogui.click()

time.sleep(3)
pyautogui.typewrite("tell me a short poem about stoicism")
pyautogui.press("enter")
time.sleep(20)

for i in range(25):
    pyautogui.moveTo(300, 200+20*i)
    pyautogui.click()

output = pyperclip.paste()

engine = pyttsx3.init()
engine.setProperty('rate', 125)
engine.say(output)
engine.runAndWait()
