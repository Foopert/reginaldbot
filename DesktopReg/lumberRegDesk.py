

# NOTE: Upon every left/right orientation, X-values seem to be changing by a factor of around ~10. This greatly affects the accuracy and produces undesired results.
#       Does this have to do with pyautogui.pause()? Time.sleep(1.3) and pyautogui.pause(1.3) seem to both have different times?
#       X-values appearing way off. I'd imagine this is runescape's doing. Or OSBuddy's.

#       UPDATE: Nevermind, looks like it has to do because I lose some orientation between the left pan and right pan. However, resetting to north after
#       each pan should keep me on track.


# Import modules
import pyautogui, time, sys

# Woodcutting bot at Varrock, near Bank of Gielinor

# Important coordinates
# COMPASS - Can differ by 8 pixels
# ~(797, 56) - Position of orientation button 
# 
# BANK - Can differ by 2 pixels
# ~(912, 235) - Position of "Bank bank booth" (closest to south door, from facing oak tree)
# ~(230, 100) - Position of bank tab 1 (where oak logs are)
# ~(245, 145) - Position of logs in bank inv
# ~(600, 68) - Position of close button
#
# TREE - Can differ by 2 pixels
# ~(430, 95) - Position of "Chop down oak" from bank booth, after orientation
# ~(419, 102)
# 
# INVENTORY - Can differ by 10 pixels
# ~(645, 1015) - Position of inventory button
# ~(915, 970) - Position of last inventory item (should be last oak log)
#
# Important Notes: Takes ~53 seconds to smelt 23 gold necklaces. Crafting levelup can popup at anytime
# and interrupt this process. Press spacebar 3-5 times to skip over this.
#
# Other bots? Progpmaker and Hoontar00
#
# 1.3 seconds after each command, DO NOT CHANGE, WILL AFFECT CAMERA ORIENTATION
#pyautogui.PAUSE = 1.3
# Handle emergency termination (move mouse to upper left of screen)
pyautogui.FAILSAFE = True

print('Cutting oak logs. Press Ctrl-C to quit.')
print("Starting reginald in...\n")
for i in range(5,0,-1):
    print(i, end='')
    print('\b' * len(str(i)), end='', flush=True)
    time.sleep(1)

# Orients camera north
print("Orienting...\n")
pyautogui.click(1756, 54)
# pyautogui.scroll(-100) # Ensure that game is scrolled out as far as possible

pyautogui.keyDown('up')
time.sleep(1.3)
pyautogui.keyUp('up')
time.sleep(0.3)
try:
    while i < 3:
        pyautogui.keyDown('right')
        time.sleep(1.3)
        pyautogui.keyUp('right')
        time.sleep(5)
        pyautogui.click(866, 103) # Travels to oak to proper place (from bank 2nd booth)
        
        for i in range(15,0,-1):
            numStr = "Walking to oak tree... " + str(i).rjust(4)
            print(numStr, end='')
            print('\b' * len(numStr), end='', flush=True)
            time.sleep(1)
        print("\n")
        pyautogui.moveTo(989,488) # Hover over chop
        for i in range(1,3,+1):
            pyautogui.click(989,488) #Clicking on stump (doesnt move)
            numStr = "Chopping" + str(i).rjust(4) + " times..."
            print(numStr, end='')
            print('\b' * len(numStr), end='', flush=True)
            time.sleep(5)
        print("\n")

         # Spacing in case of levelup (Might not be necessary)
        # pyautogui.press('space')
        # pyautogui.press('space')
        # pyautogui.press('space')
        time.sleep(0.5)
        pyautogui.keyDown('left') # Reorient to bank
        pyautogui.keyUp('left') # Reorient to bank
        time.sleep(0.5)

        pyautogui.moveTo(1291,153) # Hover over bank booth button
        pyautogui.click(1291,153) # Click bank booth

        for i in range(15,0,-1):
            numStr = "Walking to bank... " + str(i).rjust(4)
            print(numStr, end='')
            print('\b' * len(numStr), end='', flush=True)
            time.sleep(1)
        print("\n")

        print("Depositing...")
        pyautogui.click(1792,755) # First oak log
        time.sleep(0.2)
        pyautogui.click(1076,69) # Bank menu close button
        print("\n")
        i+=1



    
    # Having trouble implementing screencapture
    # pyautogui.moveTo(989,488) # Hover over oak button
    # time.sleep(3)
    # oakButtonLocation = pyautogui.locateOnScreen('ChopOakPic.PNG', region=(990, 505, 200, 200))
    # print(oakButtonLocation)

    
    #(1332,181) Clicking on Bank Bank Booth from stump
 #   for i in range(3,0,-1): 
        # Testing
  #      pyautogui.keyDown('right')
   #     pyautogui.keyUp('right')
    #    pyautogui.keyDown('left')
     #   pyautogui.keyUp('left')

except KeyboardInterrupt:
    print('\nAbort.')