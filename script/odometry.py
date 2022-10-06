import motor
from plotter import Plotter
from kinematic import angle_diff, next_position
import numpy as np
from constants import R

if __name__=="__main__":
    P = np.array([0, 0, 0])
    plotter = Plotter(1000, 1000, 6)
    m = motor.motor()
    posa_a, pos_b = m.get_position()
    while(True):
        pos_a_new, pos_b_new = m.get_position()

        plotter.plot2(P[0], P[1])
        P = next_position(P, R * angle_diff(pos_a_new, posa_a), -R * angle_diff(pos_b_new, pos_b))
        posa_a = pos_a_new
        pos_b = pos_b_new