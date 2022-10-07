import sys

import motor
import cv2
import numpy as np
from colors import Colors
from autopilot import Autopilot
from kinematic import speed_control
from suiviLigne import *
from kinematic import angle_diff, next_position
from constants import R

MODE = "RACING"
(COLOR_START, COLOR_END) = Colors.RED.value
VID_WIDTH = 600
TARGET_X = VID_WIDTH // 2
MAX_SPEED = 1
DELTA_MAX = 1000

if __name__ == "__main__":

    if sys.argv.__len__() == 2:
        MODE = sys.argv[1]
    elif sys.argv.__len__() == 3:
        color = sys.argv[2]
        if color == "RED":
            (COLOR_START, COLOR_END) = Colors.RED.value
        if color == "BLUE":
            (COLOR_START, COLOR_END) = Colors.BLUE.value
        if color == "GREEN":
            (COLOR_START, COLOR_END) = Colors.GREEN.value
        if color == "BLACK":
            (COLOR_START, COLOR_END) = Colors.BLACK.value

    robot = motor.motor()
    cam = cv2.VideoCapture(0)
    VID_WIDTH = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
    TARGET_X = VID_WIDTH // 2
    autopilot = Autopilot(MAX_SPEED, DELTA_MAX)

    
    P = np.array([0, 0, 0])
    pos_a, pos_b = robot.get_position()
    L=[]
    L.append(P)

    try:
        while True:
            (y, x) = position(np.array(COLOR_START), np.array(COLOR_END), cam)

            print(TARGET_X, " ", VID_WIDTH, " ",x)

            delta = TARGET_X - x
            a = 0.001
            b = 1000
            c = 5
            print(delta)
            [speed_1, speed_2] = speed_control(a * delta, np.exp(-delta*delta/b/b) * c)

            print(speed_1, " ", speed_2)
            robot.move(left_value=speed_1, right_value=speed_2)
            
            pos_a_new, pos_b_new = robot.get_position()

            P = next_position(P, R * angle_diff(pos_a_new, posa_a), -R * angle_diff(pos_b_new, pos_b))
            posa_a = pos_a_new
            pos_b = pos_b_new
    finally:
        print("exit")
        cam.release()
        cv2.destroyAllWindows()
        robot.stop()
        robot.unclock()
        with open("main.txt", 'w') as fp:
            for i in range(len(L)):
                for j in range(len(L[i])):
                    fp.write(str(L[i][j]))
                    if(j < len(L[i]) - 1):
                        fp.write(" ")
                if(i < len(L) - 1):
                    fp.write("\n")
