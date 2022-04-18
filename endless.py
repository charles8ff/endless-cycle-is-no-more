import pyautogui as pya
import time
import keyboard

# mySave = Mi4wNDN8fDE2NDk4MzA5Mjc0ODQ7MTYzMTYxNjk1OTAyMDsxNjUwMjY4Mzk3NTEyO1RYSVNQSVRBUzt1eGlubXwwMTExMTAwMTExMTAwMDAwMDExMTAxMDAwMHwxLjkwNzgyMzUzMzMxNTc5NGUrNTQ7Mi41MTQ5NjM1MTg1MzM2NDFlKzU2OzEzMTA7NTg2MjsyLjQ5NTc1ODc3MzQxNDMyMDRlKzU2Ozc3MDc7NDsxNjs0LjM4ODM1MDAyNjY2MjQ3MmUrNTc7MzsxMTswOzA7LTE7MTAwMDs3NTsxLjMzMjY4MTE2NDU3NzMzMjRlKzUzOzIxODsxNDsxNDstMTszOzs5LjU5OTM5MDA0NjYzMzIwMmUrNTM7MTI7MTYzNzE5NTA0MDA0OTc4NzsxNjM0OTU3NzkyMjczNjk1OzIyMzcyNDc3NzYwOTI7MDswOzYxMzs3MTY7NjQxOzIyNjs2OTg7MjU7MTsxNTswOzcwOzA7MDsxMTc7MzIzOzE2NTAyMDQwMzMxODI7MDswOzIyNywxNjY7NzM7MTsxOzEuNTA5NzgyOTU3MjkyNDQ5OGUrNDg7MDt8ODQwLDMwNDAsNC4xOTIzNjY2Nzk4NjY1ODk2ZSs1MSwxMiwsMCw4NDA7ODIwLDExNzAsMy4zOTA2MTE5MDE0MTc5NzllKzUxLDMsLDEsODIwOzgwMCwxMTUwLDguNTQzMDEwNzE0MzU3OTQzZSs0NywxMCwxNjUwMjY4NTQ1MTk1OjE6MTY1MDIzMjU1MTEwOTowOjEwMDozNjA0OjE6NToxNjQ5ODMwOTI3NDkwOiAxMTExMTAxMDExMTExMTAwMDAwMDEwMDEwMDAwMDAwMDAwIDA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDozOjQxOjA6MDowOjA6MzozNDowOjA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDowOjM6NDA6MDowOjg6NDM6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDowOjA6MDosMCw4MDA7NzgwLDExMzAsNy45MzkzMDE0NTE2MDI0NGUrNDksMCwsMSw3ODA7NzcwLDExMjAsMS4zODg2MjA2MzI3OTM3NDk2ZSs0OSwwLCwxLDc3MDs3NTAsMTEwMSwzLjAyOTEzMzc5NzQxNjkzNWUrNDgsMyw1Ojg1OjA6MTc2ODY2LjcxODY0MzM4NzE0OjE6IDI2Nzg6NTotMzU6NToxNTM1OjA6MCE0NjQ6MjotNDI6MTEzOjE0MjA6MDowITUxODoyOi02MDozNDM6MTQwNTowOjAhNzEzNToxOjU2Ojk6MDoxOjAhNjU5Njo1Oi0xNTo0MjI6MDoxOjAhODgyNjoxOjQ1OjI3OTowOjE6MCE3MDU3OjU6MTY6MTcyOjA6MTowITEwNTk1OjE6Nzc6NTYzOjA6MTowITEwOTI6NDotMTUwOjczOjEyNzU6MDowITEwOTYwOjE6Mzo4MzowOjE6MCExMjM2NjoxOjExOjQ4NTowOjE6MCExMjE2MzowOi0xMTo0NDY6MDoxOjAhMTM5MDM6MTo5OjE1MjowOjE6MCExMzY2Njo1OjIxOjE4MzowOjE6MCExMjA4MDoyOi03NDoxMTU6MDoxOjAhMTYwMzI6MDoyOjU2NjowOjE6MCEgMSwwLDc1MTs3NDAsMTA5MCwxLjI3MTc4NjQ2MDY3NTA3NGUrNDksMiw5LzgvNiAzIDE2NTAyMTAzNjAyNjkgMSwwLDc0MDs3MjAsMjE2NiwyLjQ4OTU3NDIyMzk2MzEwMDVlKzQ4LDMsNTQuMTc1MjEzMjAwMTAwOTA2IDI2IDIxNzkgMSwwLDcyMDs3MDAsMTA1MCwxLjA4NzUyMzk2NDA2MDA4MTVlKzQ4LDEsLDEsNzAwOzY5MCwxMDQwLDQuNzE4MzkwMjUzNjI2NTA1NGUrNDgsMSwsMSw2OTA7NjcwLDEwMjAsOC4zOTY1MjA4MjE2MDg5ODJlKzUwLDIsLDEsNjcwOzY2MCwxMDEwLDEuOTAzNTE4ODE0MjkzOTYyZSs1MCwyLCwxLDY2MDs2NTAsMTAwMCwxLjk0NjMyMzc1NDUxNTY4NzRlKzUxLDIsLDEsNjUwOzYzMCw5ODAsOS4zMDQ5MjQwMTAxOTkyZSs1MSwyLCwxLDYzMDs2MjAsOTcwLDIuNzYwNzM5NTc1MzI3NjAxZSs1MiwxLCwxLDYyMDs2MDAsOTUwLDEuODM3NzgyMjk1NzA4OTExOGUrNTMsMSwsMSw2MDA7NTcwLDkyMCwzLjM5MDE0NDE5NTY3OTUzMTVlKzUyLDEsLDEsNTcwOzU1MCwxMDAyLDMuMDk0NjQxMjI5NzQwNTIyNWUrNTMsMSwsMSw1NTA7fDExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMDExMTExMTExMDAxMTExMTEwMDEwMTExMTExMTExMTExMDAxMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMDAxMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMDAxMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTEwMDExMTExMTExMTExMTExMTExMTExMTExMTExMTExMDEwMTAxMDAwMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMDAxMDExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMDExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMDEwMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTAxMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTEwMDAwMTExMTExMTExMTExMTExMTExMTExMTExMTExMTEwMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMDExMTExMTExMTExMTAwMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMDExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTEwMDExMTExMTAwMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTAxMDEwMDAxMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTAwMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMDAwMDAwMDAxMTExMTExMXwxMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMDExMTExMTExMTExMTExMDExMTExMTEwMDAwMDAwMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMDExMDExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTAxMDAwMDAwMDAwMDAxMTExMTExMTExMTExMTEwMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMDExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMDExMTExMTExMTExMTExMTExMTEwMTExMTExMTExMTExMTExMDExMTExMTExMDExMTExMTExMTExMTExMTExMTAxMTExMTExMTExMTExMTExMTExMTExMTExMTExMTAxMTEwMTExMTAxMTAwMDAxfHxDQ1NFOnsidmVyc2lvbiI6IjIuMDMxIiwiQWNoaWV2ZW1lbnRzIjp7fSwiVXBncmFkZXMiOnt9LCJCdWlsZGluZ3MiOnt9LCJCdWZmcyI6e30sIlNlYXNvbnMiOnt9LCJPdGhlck1vZHMiOnt9LCJ2YXVsdCI6W10sInBlcm1hbmVudFVwZ3JhZGVzIjpbLTEsLTEsLTEsLTEsLTFdLCJjaGltZVR5cGUiOiJDaGltZSIsIm1pbGtUeXBlIjoiTWlkbmlnaHQgbWlsayIsImJnVHlwZSI6IkJsYWNrIn07SG9ydGljb29raWU6eyJhaE5ldyI6MSwiYWhKdWljeSI6MSwiYWhVcGdyYWRlIjowfTtkcnBwbHVzOnsiVVNFX0xPTkdfU0NBTEUiOjEsIk1PREUiOjZ9O0ZvcnR1bmUgQ29va2llOnsic3BlbGxGb3JlY2FzdExlbmd0aCI6MjAsInNpbUdDcyI6MCwiY29sb3JPdmVycmlkZSI6eyJCdWlsZGluZyBTcGVjaWFsIjoiI0ZGMDBGRiIsIkNsaWNrIEZyZW56eSI6IiM0QkI4RjAiLCJFbGRlciBGcmVuenkiOiIjRTFDNjk5IiwiRnJlZSBTdWdhciBMdW1wIjoiI0RBQTU2MCJ9LCJmb3JlY2FzdERyYWdvbkRyb3AiOnRydWV9O2dub3RpOjE7Y29vbGVyIHNhbXBsZSBtb2Q6MDtNRVRBOkNDU0UsKnNhbXBsZSBtb2QsKmxhbmcgc2FtcGxlIG1vZCwqY29vbGVyIHNhbXBsZSBtb2QsZ25vdGksSG9ydGljb29raWUsZHJwcGx1cyxGb3J0dW5lIENvb2tpZSxNYXhCdXR0b25SZXN0b3Jlcjs%3D%21END%21

# control variables 
curretResolutionX = 1
curretResolutionY = 1
controller = True # manual stop if needed, pressing q
loops = 1
targetAscensions = 1000 # change this number if you don't need to do 1000 ascensions
endingDelay = loops * 0.05 # adds a delay before ascending

tinySleep = 0.2
mediumSleep = 0.8

# relative % , commented the pixel measures in 1920*1080
column = 0.9115 # column = 1750 
upgrades = 0.1389 # upgrades = 150 
cursors = 0.2870 # cursors = 310 
grandmas = 0.3516 # grandmas = 380
fractals = 0.7778 # fractals = 840 
idleverses = 0.8889 # idleverses = 960
legacyX = 0.8073 # legacyX = 1550
legacyY = 0.0741 # legacyY = 80
reincarnateX = 0.4922 # reincarnateX = 945
reincarnateY = 0.1016 # reincarnateY = 110

def buy100s():
    pya.keyDown('shift')
    pya.click()
    time.sleep(tinySleep)
    pya.click()
    time.sleep(tinySleep)
    pya.click()
    pya.keyUp('shift')

def buyUpgrades():
    pya.press('home') # this key scrolls up
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
    buyUpgrades() # scrolls auto up again  
    time.sleep(mediumSleep) 
    pya.moveTo(column, cursors, duration = 0)
    buy100s()
    pya.moveTo(column, grandmas, duration = 0)
    buy100s()
    time.sleep(mediumSleep) 
    buyUpgrades()
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
        print('Key \'q\' pressed, Handmade stopped after the ascension.')
        global controller
        controller = False

# adding a wrapper function 
def oneRound():
    buyBuildings()
    stop() # press q

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

print('Starting in 3')
time.sleep(3)
# starts in 3 seconds, tab into CookieClicker

while controller and loops <= targetAscensions:
    # add more oneRounds if you don't achieve +1 prestige with 2 of them
    oneRound()
    oneRound() 
    time.sleep(mediumSleep)
    buyUpgrades()
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