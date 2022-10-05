import motor

if __name__ == "__main__" :

    robot = motor()
    try :
        while True:
            robot.move(left_value=6, right_value=6) #rad/s

    finally:
        robot.stop()
        robot.unclock()
