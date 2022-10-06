import sys

import motor
import cv2
import numpy as np
from colors import Colors
from autopilot import Autopilot
from suiviLigne import *

MODE = "RACING"
(COLOR_START, COLOR_END) = Colors.RED.value
VID_LENGTH = 300
VID_WIDTH = 600
(TARGET_X, TARGET_Y) = (VID_WIDTH // 2, 0)
MAX_SPEED = 5
DELTA_MAX = 100
# RED_START = np.array([0,100,100])
# RED_END = np.array([10,255,255])
#
# YELLOW_START = np.array([20,100,100])
# YELLOW_END = np.array([30,255,255])
#
# ORANGE_START = np.array([10,100,20])
# ORANGE_END = np.array([25,255,255])
#
# BLACK_START = np.array([0,0,0])
# BLACK_END = np.array([180,255,30])

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

    print(COLOR_START)

    robot = motor.motor()
    cam = cv2.VideoCapture(0)
    VID_WIDTH = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
    VID_HEIGHT = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
    autopilot = Autopilot(MAX_SPEED, DELTA_MAX)

    try:
        speed_1, speed_2 = autopilot.init_speed()
        robot.move(left_value=speed_1, right_value=speed_2)

        while True:
            print(speed_1, " ", speed_2)

            (x, y) = position(np.array(COLOR_START), np.array(COLOR_END), cam)
            print(x, " ", y)
            delta = np.sqrt(np.power(TARGET_X - x, 2) + np.power(TARGET_Y - y, 2))
            speed_1, speed_2 = autopilot.compute_speed(delta)
            robot.move(left_value=speed_1, right_value=speed_2)

            # if cv2.waitKey(1) & 0xFF == ord('C'):
            #     break
    finally:
        print("exit")
        cam.release()
        cv2.destroyAllWindows()
        robot.stop()
        robot.unclock()
