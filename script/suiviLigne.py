from turtle import pos
import cv2
import numpy as np

def position(color_start, color_end, cam):
  A = 0
  B = 0

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

  cv2.imshow('new_video',mask)

  return (position_x, position_y)
