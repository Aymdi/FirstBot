from turtle import pos
import cv2
import numpy as np

RED_START = np.array([0,100,100])
RED_END = np.array([10,255,255])

YELLOW_START = np.array([20,100,100])
YELLOW_END = np.array([30,255,255])

ORANGE_START = np.array([10,100,20])
ORANGE_END = np.array([25,255,255])

BLACK_START = np.array([0,0,0])
BLACK_END = np.array([180,255,30])

A = 0
B = 0

def ligne(color_start, color_end):
  cam = cv2.VideoCapture(0)

  while(True):
      _, img = cam.read()
      
      hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
      mask = cv2.inRange(hsv, color_start , color_end)

      # ligne de test allant de mask[0,0] à mask[img.shape[0],0]
      for y1 in range (0,img.shape[0]):
        if(mask[0,y1] == 255):
          A = y1
          break

      for y2 in range (img.shape[0],0, -1):
        if(mask[0,y2] == 255):
          B = y2
          break

      position_x = 0
      position_y =(A + B)/2

      print(position_x, position_y)
    
    
      cv2.imshow('new_video',mask)

      if cv2.waitKey(1) & 0xFF == ord('C'):
        break

  cam.release()

  cv2.destroyAllWindows() 

#toto = ligne(RED_START,RED_END)
