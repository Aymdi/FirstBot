import motor
from plotter import Plotter
from kinematic import angle_diff, next_position, point_to_point, speed_control
import numpy as np
from constants import R


if __name__=="__main__":
    P = np.array([0, 0, 0])
    plotter = Plotter(1000, 1000, 6.0)
    m = motor.motor()

    target_x = float(input("Target X coordinate :"))
    target_y = float(input("Target Y coordinate :"))
    target_z = float(input("Target orientation :"))

    posa_a, pos_b = m.get_position()
    try:
        while(True):
            pos_a_new, pos_b_new = m.get_position()
            P = next_position(P, R * angle_diff(pos_a_new, posa_a), -R * angle_diff(pos_b_new, pos_b))
            plotter.plot2(P[0], P[1])
            posa_a = pos_a_new
            pos_b = pos_b_new

            err_o, err_d = point_to_point(np.array([target_x, target_y]), P)
            #print(P)

            [speed_left, speed_right] = speed_control(0.4*err_o, 0.5*err_d)
            #print([speed_left, speed_right])
            m.move(speed_left, speed_right)

    finally:
        m.stop()
        m.unclock()