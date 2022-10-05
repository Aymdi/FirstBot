import motor
from suiviLigne import *

RED_START = np.array([0,100,100])
RED_END = np.array([10,255,255])

YELLOW_START = np.array([20,100,100])
YELLOW_END = np.array([30,255,255])

ORANGE_START = np.array([10,100,20])
ORANGE_END = np.array([25,255,255])

BLACK_START = np.array([0,0,0])
BLACK_END = np.array([180,255,30])

if __name__ == "__main__" :
    
    robot = motor.motor()
    cam = cv2.VideoCapture(0)
    
    try :
        while True:
            robot.move(left_value=6, right_value=6) #rad/s
            (x, y) = position(RED_START,RED_END, cam) 
            
            if cv2.waitKey(1) & 0xFF == ord('C'):
                break
            

    finally:
        cam.release()
        cv2.destroyAllWindows() 
        robot.stop()
        robot.unclock()
