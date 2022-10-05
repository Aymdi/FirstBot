import motor
from getkey import getkey, keys


if __name__ == "__main__" :

    robot = motor.motor()
    
    try :
        while True:
            key = getkey()
            left_value, right_value = 6, 6 #rad/s
            if key == "z":
                robot.move(left_value, right_value)
            elif key == "d":
                robot.move(left_value, 0)
            elif key == "q":
                robot.move(0, right_value)
            elif key == "s":
                robot.move(-left_value, -right_value)
            elif key == "p":
                robot.move(0, 0)

    finally:
        robot.stop()
        robot.unclock()

