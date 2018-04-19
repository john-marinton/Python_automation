import pyautogui
import time

distance=200
time.sleep(2)
##while distance>0:
##   pyautogui.dragRel(distance,0)
##   pyautogui.dragRel(0,distance)
##   pyautogui.dragRel(-distance,0)
##   distance=distance-20  
##   pyautogui.dragRel(0,-distance)
##   pyautogui.dragRel(distance,0)
##   distance=distance-20
##   pyautogui.dragRel(0,distance)
##   pyautogui.dragRel(-distance,0)
##   distance=distance-20
##   pyautogui.dragRel(0,-distance)
##   pyautogui.dragRel(distance,0)
##   distance=distance-20
##   pyautogui.dragRel(0,distance)
##   pyautogui.dragRel(-distance,0)
##   distance=distance-20
##   pyautogui.dragRel(0,-distance)
##   pyautogui.dragRel(distance,0)
##   distance=distance-20
##   pyautogui.dragRel(0,distance)
##   pyautogui.dragRel(-distance,0)
##   distance=distance-20
##   pyautogui.dragRel(0,-distance)
##   pyautogui.dragRel(distance,0)
##   distance=distance-20
##   pyautogui.dragRel(0,distance)
##   pyautogui.dragRel(-distance,0)
##   distance=distance-20
##   pyautogui.dragRel(0,-distance)
##   pyautogui.dragRel(distance,0)
##   distance=distance-20
##   pyautogui.dragRel(0,distance)
##   pyautogui.dragRel(-distance,0)
##   distance=distance-20
##   pyautogui.dragRel(0,-distance)
##   break                                         #----if i include break here have to do it like this

#----------------------------or-------------------------------

while distance>0:
   pyautogui.dragRel(distance,0)
   distance=distance-20
   pyautogui.dragRel(0,distance)
   pyautogui.dragRel(-distance,0)
   distance=distance-20
   pyautogui.dragRel(0,-distance)



