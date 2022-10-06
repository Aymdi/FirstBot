import sys

import motor
import cv2
import numpy as np
from colors import Colors
from autopilot import Autopilot
from kinematic import speed_control
from suiviLigne import *

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

    try:
        while True:
            (y, x) = position(np.array(COLOR_START), np.array(COLOR_END), cam)

            print(TARGET_X, " ", VID_WIDTH, " ",x)

            delta = x - TARGET_X
            a = 0.0001
            b = 150
            print(delta)
            [speed_1, speed_2] = speed_control(a * delta, 1/(np.absolute(delta) + 1) * b)

            print(speed_1, " ", speed_2)
            robot.move(left_value=speed_1, right_value=speed_2)
    finally:
        print("exit")
        cam.release()
        cv2.destroyAllWindows()
        robot.stop()
        robot.unclock()
