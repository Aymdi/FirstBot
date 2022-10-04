import cv2
import numpy as np

cam = cv2.VideoCapture(0)
xvid = cv2.VideoWriter_fourcc(*'XVID')
video= cv2.VideoWriter('captured_video.avi', xvid, 10, (500,300))

while(True):
    _, img = cam.read()
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    red_start = np.array([0,100,100])
    red_end = np.array([10,255,255])

    mask = cv2.inRange(hsv, red_start, red_end)
    new_video = cv2.bitwise_and(img, img, mask= mask)
    video.write(img)
  
    cv2.imshow('new_video',new_video)

    if cv2.waitKey(1) & 0xFF == ord('C'):
      break

cam.release()
video.release()

cv2.destroyAllWindows() 
