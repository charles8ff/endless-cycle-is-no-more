import pyautogui as pya
import time
import keyboard

# made this measures in 1980*1080, feel free to change for other resolutions
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
loops = 1
targetAscensions = 1000 # change this number if you don't need to do 1000 ascensions
endingDelay = loops * 0.05 # adds a delay before ascending

tinySleep = 0.2
mediumSleep = 0.5


def buy100s():
    pya.keyDown('shift')
    pya.click()
    time.sleep(tinySleep)
    pya.click()
    time.sleep(tinySleep)
    pya.click()
    pya.keyUp('shift')

def buyupgrades():
    pya.press('home') # this key scrolls up
    time.sleep(mediumSleep)
    pya.moveTo(column, upgrades, duration = 0)
    pya.click()
    time.sleep(mediumSleep)
    pya.click()
    time.sleep(mediumSleep)
    pya.click()
    pya.moveTo(column, upgrades, duration = 0)
    
def buyBuildings():
    time.sleep(mediumSleep)
    buyupgrades() # scrolls auto up again  
    time.sleep(mediumSleep) 
    pya.moveTo(column, cursors, duration = 0)
    buy100s()
    pya.moveTo(column, grandmas, duration = 0)
    buy100s()
    time.sleep(mediumSleep) 
    buyupgrades()
    pya.moveTo(column, grandmas, duration = 0)
    pya.click()
    pya.press('end')  # scroll down again
    time.sleep(1)
    pya.moveTo(column, fractals, duration = 0)
    buy100s()
    pya.moveTo(column, idleverses, duration = 0)
    buy100s()
    
# adding a manual stop, this will finish the ascension and stop from looping
def stop():
    if keyboard.is_pressed('q'):
        print('Handmade Stop')
        global controller
        controller = False

# adding a wrapper function 
def oneRound():
    buyBuildings()
    stop() # press q
    
time.sleep(3)      
# starts in 3 seconds, tab into CookieClicker
while controller and loops <= targetAscensions:
    # add more oneRounds if you don't achieve +1 prestige with 2 of them
    oneRound()
    oneRound() 
    time.sleep(mediumSleep)
    buyupgrades()
    stop() # press q
    time.sleep(1+endingDelay) # maybe this delay is not needed depending on your prestige level
    # reincarnation
    pya.press('home')
    time.sleep(0.2)
    pya.moveTo(legacyX, legacyY, duration = 0)
    pya.click()
    time.sleep(0.5)
    pya.press('enter')
    time.sleep(0.5)
    pya.press('esc')
    pya.moveTo(reincarnateX, reincarnateY, duration = 0)
    pya.click()
    pya.press('enter')
    loops+=1 # loop counter