import motor
from plotter import Plotter
from kinematic import angle_diff, next_position, point_to_point, speed_control
import numpy as np
from constants import R


if __name__=="__main__":
    P = np.array([0, 0, 0])
    m = motor.motor()

    target_x = float(input("Target X coordinate :"))
    target_y = float(input("Target Y coordinate :"))

    posa_a, pos_b = m.get_position()
    L=[]
    L.append(P)
    try:
        while(True):
            pos_a_new, pos_b_new = m.get_position()
            P = next_position(P, R * angle_diff(pos_a_new, posa_a), -R * angle_diff(pos_b_new, pos_b))
            posa_a = pos_a_new
            pos_b = pos_b_new

            L.append(P)

            err_o, err_d = point_to_point(np.array([target_x, target_y]), P)
            #print(P)

            if(abs(err_d) >= 0.2):
                [speed_left, speed_right] = speed_control(0.4*err_o, 0.5*err_d + 0.1)
                #print([speed_left, speed_right])
                m.move(speed_left, speed_right)

    finally:
        m.stop()
        m.unclock()
        with open("target.txt", 'w') as fp:
            for i in range(len(L)):
                for j in range(len(L[i])):
                    fp.write(str(L[i][j]))
                    if(j < len(L[i]) - 1):
                        fp.write(" ")
                if(i < len(L) - 1):
                    fp.write("\n")