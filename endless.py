import pyautogui as pya
import time
import keyboard

# mySave = ;)

# Control variables 
curretResolutionX = 1
curretResolutionY = 1
controller = True # Manual stop if needed, pressing q
loops = 1
targetAscensions = 1000 # Change this number if you don't need to do 1000 ascensions
endingDelay = loops * 0.05 # Adds a delay before ascending

# Delays, modify if your PC is Fast, mine is not. Default are tiny: 0.2 seconds and medium: 0.8 seconds
tinySleep = 0.2
mediumSleep = 0.8

# Relative % , commented the pixel measures in 1920*1080
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
    pya.moveTo(column, upgrades, duration = 0)
    pya.click()
    time.sleep(mediumSleep)
    pya.click()
    time.sleep(mediumSleep)
    pya.click()
    pya.moveTo(legacyX, grandmas, duration = 0)
    
def buyBuildings():
    time.sleep(mediumSleep)
    buyUpgrades() # Scrolls auto up again  
    time.sleep(mediumSleep) 
    pya.moveTo(column, cursors, duration = 0)
    buy100s()
    pya.moveTo(column, grandmas, duration = 0)
    buy100s()
    time.sleep(mediumSleep) 
    buyUpgrades()
    pya.moveTo(column, grandmas, duration = 0)
    pya.click()
    pya.press('end')  # Scroll down again
    time.sleep(1)
    pya.moveTo(column, fractals, duration = 0)
    buy100s()
    pya.moveTo(column, idleverses, duration = 0)
    buy100s()
    
# Adding a manual stop, this will finish the ascension and stop from looping
def stop():
    if keyboard.is_pressed('q'):
        print('Key \'q\' pressed, Handmade stopped after the ascension.')
        global controller
        controller = False

# Adding a wrapper function 
def oneRound():
    buyBuildings()
    stop() # Press q!

curretResolutionX, curretResolutionY = pya.size()
print('Is your current resolution: '+ str(curretResolutionX) + ' * ' + str(curretResolutionY) + ' ?\nPress \'Enter\' to continue, press \'Control + C\' to exit')
input()

print('Calculating pixels...')
column = int( column * curretResolutionX) # 0.9114
upgrades = int( upgrades * curretResolutionY) # 0.1388
cursors = int( cursors * curretResolutionY) # 0.2870
grandmas = int( grandmas * curretResolutionY) # 0.3518
fractals = int( fractals * curretResolutionY) # 0.7778
idleverses = int( idleverses * curretResolutionY) #  0.8889
legacyX = int( legacyX * curretResolutionX) # 0.8073
legacyY = int( legacyY * curretResolutionY) # 0.0741 
reincarnateX = int( reincarnateX * curretResolutionX) # 0.4922
reincarnateY = int( reincarnateY * curretResolutionY) #  0.1018

# Starts in 3 seconds, tabs into CookieClicker
pya.hotkey('alt', 'tab')
print('Starting in 3...')
time.sleep(1)
print('Starting in 2...')
time.sleep(1)
print('Starting in 1...')
time.sleep(1.5)

while controller and loops <= targetAscensions:
    # Add more oneRounds if you don't achieve +1 prestige with 2 of them
    oneRound()
    oneRound() 
    time.sleep(mediumSleep)
    buyUpgrades()
    stop() # Press q!
    time.sleep(1+endingDelay) # Maybe this delay is not needed depending on your prestige level
    # Reincarnation sequence
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
    loops+=1 # Ascensions counter