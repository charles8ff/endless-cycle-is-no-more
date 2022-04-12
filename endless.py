import pyautogui
import time
import keyboard

column = 1750 # may not need
upgrades = 150 
cursors = 310 
grandmas = 380
fractals = 840 
idleverses = 960
controller = True
loops= 1
x = loops * 0.03

def buy100s():
    pyautogui.keyDown('shift')
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click()
    pyautogui.keyUp('shift')

def buyupgrades():
    pyautogui.press('home')
    time.sleep(0.5)
    pyautogui.moveTo(1750, upgrades, duration = 0)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.moveTo(1500, upgrades, duration = 0)
    
def buildings_loop():
    time.sleep(0.5)
    buyupgrades() # scrolls auto up again  
    time.sleep(0.5) 
    pyautogui.moveTo(1750, cursors, duration = 0)
    buy100s()
    pyautogui.moveTo(1750, grandmas, duration = 0)
    buy100s()
    time.sleep(0.5) 
    buyupgrades()
    pyautogui.moveTo(1750, grandmas, duration = 0)
    pyautogui.click()
    pyautogui.press('end')  # scroll down again
    time.sleep(1)
    pyautogui.moveTo(1750, fractals, duration = 0)
    buy100s()
    pyautogui.moveTo(1750, idleverses, duration = 0)
    buy100s()
    
def stop():
    if keyboard.is_pressed("q"):
        print("q pressed")
        global controller
        controller = False
        
#starts, tab into cookieclicker
time.sleep(3)
while controller:

    buildings_loop()
    stop()
    buildings_loop()
    stop()
    time.sleep(0.5)
    buyupgrades()
    stop()
    time.sleep(1+x)
    loops+=1
    # reincarnation
    pyautogui.press('home')
    time.sleep(0.2)
    pyautogui.moveTo(1550, 80, duration = 0)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('esc')
    pyautogui.moveTo(945, 110, duration = 0)
    pyautogui.click()
    pyautogui.press('enter')