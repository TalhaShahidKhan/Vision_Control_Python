import cv2

import numpy as np
import pyautogui


cap = cv2.VideoCapture(0)
lower_orange = np.array([0,75,75])
upper_orange = np.array([10,255,255])
prev_y = 0
while True:
  ret,frame = cap.read()
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(hsv,lower_orange,upper_orange)
  con,hir = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  for c in con:
    area = cv2.contourArea(c)
    if area>750:
      x,y,w,h = cv2.boundingRect(c)
      cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
      if y > prev_y:
        pyautogui.press('space')
      if y<prev_y:
        pyautogui.press('up')
      prev_y = y
      
      
  cv2.imshow('frame',frame)

  if cv2.waitKey(10) == ord('q'):
    break



cap.release()
cv2.destroyAllWindows()