import pyautogui
import time
x,y=pyautogui.position()
try:
    while True:
        x,y=pyautogui.position()
        if ((x>1343 and x<1732) and (y>516 and y<639)):

        #Case 1: If hit by a bird with revive

            if pyautogui.pixelMatchesColor(1492,530,(250,109,70)):
                print("I have hit a pakshi and revivable")
                time.sleep(1)
                pyautogui.moveTo(1512,621)
                pyautogui.leftClick() #No Thanks
                print("Clicked on No Thanks")
                time.sleep(1)
                pyautogui.moveTo(1508,790)
                pyautogui.leftClick() #Play again
                print("Clicked on Try Again")
                time.sleep(1)
                pyautogui.moveTo(1400,580)
                time.sleep(2)
                pyautogui.leftClick()
                time.sleep(2)
                print("Clicked")

        #Case 2: If hit by bird with no revive

            elif pyautogui.pixelMatchesColor(1442,622,(67,37,0)):
                print("I have hit a pakshi and not revivable")
                pyautogui.moveTo(1526,622)
                time.sleep(1)
                pyautogui.leftClick()
                print("Clicks")
                time.sleep(2)
                pyautogui.moveTo(1530,800)
                print("Try again")
                pyautogui.leftClick()
                time.sleep(1)
                pyautogui.moveTo(1400,580) #Start Position
                time.sleep(2)
                pyautogui.leftClick() #Starts
                print("Clicks to Start")


        #Case 3: If Valuables Secured without 3x
            
            elif pyautogui.pixelMatchesColor(1569,452,(0,38,102)):
                print("Secured without 3x")
                time.sleep(5)
                pyautogui.moveTo(1522,799) #Play again
                print("Play again")
                pyautogui.leftClick()
                pyautogui.moveTo(1532,606) #Start Position
                time.sleep(2)
                pyautogui.leftClick()
                pyautogui.leftClick() #Starts
                print("Starts")



except KeyboardInterrupt:
    print('\n')