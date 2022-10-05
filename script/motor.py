import pypot.dynamixel
import math
import time
import numpy as np
    

class motor:

    dxl_io = None

    def __init__(self):
        ports = pypot.dynamixel.get_available_ports()
        if not ports:
            exit('No port')

        self.dxl_io = pypot.dynamixel.DxlIO(ports[0])
        self.dxl_io.set_wheel_mode([1])

        self.left = 1
        self.right = 2

    def move(self, left_value, right_value):
        # leff_value and right_value in rad/s
        self.dxl_io.set_moving_speed({self.left: math.degrees(left_value)})
        self.dxl_io.set_moving_speed({self.right: math.degrees(-right_value)})

    def stop(self):
        self.dxl_io.set_moving_speed({self.left: math.degrees(0)})
        self.dxl_io.set_moving_speed({self.right: math.degrees(0)})

    def lock(self):
        self.dxl_io.enable_torque([self.left,self.right])

    def unclock(self):
        self.dxl_io.disable_torque([self.left,self.right])

    def get_speed(self):
        speeds = self.dxl_io.get_moving_speed([self.left,self.right])
        left_speed, right_speed = speeds[0], speeds[1]
        return left_speed, right_speed


if __name__=="__main__":
    motor = motor()
    motor.move(left_value=6, right_value=6) #rad/s
    time.sleep(2)
    motor.stop()
    motor.unclock()


