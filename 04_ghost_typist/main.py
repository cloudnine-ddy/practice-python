import pyautogui
import time

print("Program starting in 5s.....")
time.sleep(1)
print("Program starting in 4s.....")
time.sleep(1)
print("Program starting in 3s.....")
time.sleep(1)
print("Program starting in 2s.....")
time.sleep(1)
print("Program starting in 1s.....")
time.sleep(1)

pyautogui.write("Hello! I am a Python Ghost Typist.", interval=0.1)

pyautogui.press('enter')

pyautogui.write("I am taking over this computer...... just kidding! haha", interval=0.1)

print("Program Ended.")
