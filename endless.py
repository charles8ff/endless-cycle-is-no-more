import pyautogui
import time
import keyboard

#made this measures in 1980*1080, feel free to change for other resolutions
column = 1750 
upgrades = 150 
cursors = 310 
grandmas = 380
fractals = 840 
idleverses = 960
legacyX = 1550
legacyY = 80
reincarnateX = 945
reincarnateY = 110

controller = True # manual stop if needed, pressing q
loops= 1
endingDelay = loops * 0.05 # adds a delay before ascending

tinySleep = 0.2
mediumSleep = 0.5


def buy100s():
    pyautogui.keyDown('shift')
    pyautogui.click()
    time.sleep(tinySleep)
    pyautogui.click()
    time.sleep(tinySleep)
    pyautogui.click()
    pyautogui.keyUp('shift')

def buyupgrades():
    pyautogui.press('home')
    time.sleep(mediumSleep)
    pyautogui.moveTo(column, upgrades, duration = 0)
    pyautogui.click()
    time.sleep(mediumSleep)
    pyautogui.click()
    time.sleep(mediumSleep)
    pyautogui.click()
    pyautogui.moveTo(column, upgrades, duration = 0)
    
def buyBuildings():
    time.sleep(mediumSleep)
    buyupgrades() # scrolls auto up again  
    time.sleep(mediumSleep) 
    pyautogui.moveTo(column, cursors, duration = 0)
    buy100s()
    pyautogui.moveTo(column, grandmas, duration = 0)
    buy100s()
    time.sleep(mediumSleep) 
    buyupgrades()
    pyautogui.moveTo(column, grandmas, duration = 0)
    pyautogui.click()
    pyautogui.press('end')  # scroll down again
    time.sleep(1)
    pyautogui.moveTo(column, fractals, duration = 0)
    buy100s()
    pyautogui.moveTo(column, idleverses, duration = 0)
    buy100s()
    
#adding a manual stop, this will finish the ascension and stop from looping
def stop():
    if keyboard.is_pressed('q'):
        print('Handmade Stop')
        global controller
        controller = False
        
def oneRound():
    buyBuildings()
    stop() # press q
    
time.sleep(3)      
#starts in 3, tab into cookieclicker
while controller and loops<=1000:
    #add more oneRounds if you don't achieve +1 ascensions with 2 of them
    oneRound()
    oneRound() 
    time.sleep(mediumSleep)
    buyupgrades()
    stop() # press q
    time.sleep(1+endingDelay)
    # maybe this stop is not needed depending on your prestige
    # reincarnation
    pyautogui.press('home')
    time.sleep(0.2)
    pyautogui.moveTo(legacyX, legacyY, duration = 0)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('esc')
    pyautogui.moveTo(reincarnateX, reincarnateY, duration = 0)
    pyautogui.click()
    pyautogui.press('enter')
    #loop counter
    loops+=1