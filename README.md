# Achieving Endless Cycle Backseated
#### Run this code, leave your game overnight, get Reincarnation and Endless Cycle achievements

:cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie:

> I chose to think about a bunch of code   
> Instead of clicking a bunch of times.  
## What is this

This is a script, an automated process to ascend several times in a row. This program asks the user to record your mouse position in some key places in order to achieve ascensions without further help.

__**:warning::construction::warning: Sections below under construction :warning::construction::warning:**__
## Requirements

- Cookie Clicker Game Running
- Visual Studio Code or the IDE of your choosing
- Python installed in your computer
- Install the following requirements by copy and pasting the following on your terminal.
````
py -m install -r requirements.txt
````
Once you got everything ready, you can run the script and some following instructions will appear on the console. Follow those!
## Instructions

\-> Once the script starts, you will do an ascension alt-tabbing to the script until it gathers all the information it needs, and then it will repeat the process all the times you set it for, with the parameter _targetAscensions_. Does by default 1000 ascensions.

:exclamation::exclamation::exclamation: Remember to _**UN VAULT**_ any upgrade you might have vaulted! If the vault appears in one off the ascensions all the pots will move (because the game needs to pop the vault in between) and it might fail to ascend!

Spots that the script will ask you for:

| 1. Buy All Upgrades Button | 2. Buy Cursors Button  | 3. Buy Grandmas Button
| ------------- | ------------- | ------------- |
| <a href="https://imgur.com/qzpUl6i"><img src="https://i.imgur.com/qzpUl6i.jpg" title="source: imgur.com" /></a> | <a href="https://imgur.com/xGTRaww"><img src="https://i.imgur.com/xGTRaww.jpg?1" title="source: imgur.com" /></a> | <a href="https://imgur.com/2LwE58Q"><img src="https://i.imgur.com/2LwE58Q.jpg?1" title="source: imgur.com" /></a> |
 
:exclamation::exclamation: Now you need to scroll all the way down, you can press 'End' key (the script will do that) to record the lower building's positions. Be sure to scroll _all_ the way down.

| 4. Buy Fractals Button | 5. Buy Idleverses Button  |
| ------------- | ------------- | 
|<a href="https://imgur.com/bDozsdm"><img src="https://i.imgur.com/bDozsdm.jpg" title="source: imgur.com" /></a>  | <a href="https://imgur.com/pQ4Relh"><img src="https://i.imgur.com/pQ4Relh.jpg" title="source: imgur.com" /></a> |

Then, the 2 lasts spots are the 'Legacy' button and the 'Reincarnate' button, and that will be the final steps of the 'hand-made' ascension. After that, the script will start copying the process.

| 6. Legacy Button | 7. Reincarnate Button  |
| ------------- | ------------- | 
|<a href="https://imgur.com/HalsZm0"><img src="https://i.imgur.com/HalsZm0.jpg" title="source: imgur.com" /></a>  | <a href="https://imgur.com/kWjBlW3"><img src="https://imgur.com/kWjBlW3.jpg" title="source: imgur.com" /></a> |

And everything's ready! :sunglasses: Now the script will start to run when you press 'Enter'.

The script takes into account this first ascension and does the remaining ones depending how many you asked it to do in the _targetAscensions_ field.
## Advanced tips

\-> Speed of the script may be improved (99% sure by a lot), but my laptop lagged so it might be slower than needed. Change _tinySleep_, _mediumSleep_ or _endingDelay_ and test your setup. Both your pc performance and the prestige levels you already have will affect how fast you can ascend. Remember prestige scales, and in 1000 ascensions it _does_ scale.

````
Package Versions:
- Python: 3.10 (with modules time and threading)
- PyAutoGUI: 0.9.53
- keyboard: 0.13.5
````

> Inspired by Pegasus280.
