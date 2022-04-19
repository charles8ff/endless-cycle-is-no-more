import threading
import time

import keyboard
import pyautogui as pya

# mySave = ;)

# Control variables 
loops = 1
targetAscensions = 1000 # Change this number if you don't need to do 1000 ascensions
endingDelay = loops * 0.05 # Adds a delay before ascending

# Delays, modify if your PC is Fast, mine is not. Default are tiny: 0.2 seconds and medium: 0.8 seconds
tinySleep = 0.2
mediumSleep = 0.8

<<<<<<< HEAD
# Where the coords will be stored
spotsDict = dict(
        BuyAllUpgrades = (0,0),
        Cursors = (0,0),
        Grandmas = (0,0),
        Fractals = (0,0),
        Idleverses = (0,0),
        LegacyButton = (0,0),
        ReincarnateButton = (0,0)
        )
=======
# Relative % , commented the pixel measures in 1920*1080
<<<<<<< HEAD
column = 0.9115 # column = 1750px / 1920
upgrades = 0.1389 # upgrades = 150px / 1080
cursors = 0.2870 # cursors = 310px / 1080
grandmas = 0.3516 # grandmas = 380px / 1080
fractals = 0.7778 # fractals = 840px / 1080
idleverses = 0.8889 # idleverses = 960px / 1080
legacyX = 0.8073 # legacyX = 1550px / 1920
legacyY = 0.0741 # legacyY = 80px / 1080
reincarnateX = 0.4922 # reincarnateX = 945px / 1920
reincarnateY = 0.1016 # reincarnateY = 110px / 1080
=======
column = 0.9115 # column = 1750 / 1920
upgrades = 0.1389 # upgrades = 150 / 1080
cursors = 0.2778 # cursors = 300 / 1080 
grandmas = 0.3334 # grandmas = 360 / 1080
fractals = 0.7963 # fractals = 860 / 1080
idleverses = 0.9074 # idleverses = 980 / 1080
legacyX = 0.7969 # legacyX = 1530 / 1920
legacyY = 0.0694 # legacyY = 75 / 1080
reincarnateX = 0.4948 # reincarnateX = 950
reincarnateY = 0.1018 # reincarnateY = 110
>>>>>>> cbc04d6b2b66548ba868f4457db4bf5c617c0c6b
>>>>>>> main

# Functions
def buy100s():
    pya.keyDown('shift')
    pya.click()
    time.sleep(tinySleep)
    pya.click()
    time.sleep(tinySleep)
    pya.click()
    pya.keyUp('shift')

def buyUpgrades():
    pya.press('home') # This key scrolls up
    time.sleep(mediumSleep)
    pya.moveTo(spotsDict['BuyAllUpgrades'], duration = 0)
    pya.click()
    time.sleep(mediumSleep)
    pya.click()
    time.sleep(mediumSleep)
    pya.click()
    pya.moveTo(spotsDict['ReincarnateButton'], duration = 0)
    
def buyBuildings():
    time.sleep(mediumSleep)
    buyUpgrades() # Scrolls auto up again  
    time.sleep(mediumSleep) 
    pya.moveTo(spotsDict['Cursors'], duration = 0)
    buy100s()
    pya.moveTo(spotsDict['Grandmas'], duration = 0)
    buy100s()
    time.sleep(mediumSleep) 
    buyUpgrades()
    pya.moveTo(spotsDict['Grandmas'], duration = 0)
    pya.click()
    pya.press('end')  # Scroll down again
    time.sleep(1)
    pya.moveTo(spotsDict['Fractals'], duration = 0)
    buy100s()
    pya.moveTo(spotsDict['Idleverses'], duration = 0)
    buy100s()
    
# Adding a manual stop, this will finish the ascension and stop from looping
def stop():
    controller = True
    while controller:
        if keyboard.is_pressed('q'):
            print('\t> Key \'q\' pressed, Handmade stopped')
            controller = False
            altTabTo('last')
            pya.moveTo(0, 0, duration = 0)
    
# Tab function
def altTabTo(window):
    if window == 'last':
        pya.hotkey('alt', 'tab')
    else:
        pya.getWindowsWithTitle(window)[0].minimize()
        pya.getWindowsWithTitle(window)[0].maximize()
        
########################################################################### Start
thread = threading.Thread(target=stop)

print('\n\nWelcome to charles8ff\'s Endless Cycle Is No More! '
      'This is an script, it will perform automatic actions. Do not fear it.'
      '\nNow we need some locations of your screen...\n')
# Loop the dict to record coords
for item in spotsDict:
    print('In your game, move your cursor where the '+ item + ' is. '
          'When ready, press \'Spacebar\' to record '+ item + '\'s position in your screen.')
    print('Press \'Enter\' to alt-tab to Cookie Clicker.\n\t>')
    input()
    altTabTo('Cookie Clicker')
    done = False
    while not done:
        if keyboard.is_pressed('space'):
            x, y = pya.position()
            spotsDict[item]= x, y
            print(item +'\'s location saved!\n\n')
            done = True
            altTabTo('last')

print('Press \'Enter\' to start the fun.\n\t')   
input()
thread.start()
altTabTo('Cookie Clicker')
pya.moveTo(spotsDict['ReincarnateButton'], duration = 0)
pya.click()
pya.press('enter')

while loops <= targetAscensions:
    # Add more buyBuildings if you don't achieve +1 prestige with 2 of them
    buyBuildings()
    buyBuildings() 
    time.sleep(mediumSleep)
    buyUpgrades()
    time.sleep(1+endingDelay) # Maybe this delay is not needed depending on your prestige level
    # Reincarnation sequence
    pya.press('home')
    time.sleep(0.2)
    pya.moveTo(spotsDict['LegacyButton'], duration = 0)
    pya.click()
    time.sleep(0.5)
    pya.press('enter')
    time.sleep(0.5)
    pya.press('esc')
    pya.moveTo(spotsDict['ReincarnateButton'], duration = 0)
    pya.click()
    pya.press('enter')
    loops+=1 # Ascensions counter
    print('ASCENSIONS REMAINING: '+ str(targetAscensions-loops) +'!!!')
