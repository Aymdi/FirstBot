import motor
from plotter import Plotter
from kinematic import angle_diff, next_position
import numpy as np
from constants import R

if __name__=="__main__":
    P = np.array([0, 0, 0])
    m = motor.motor()
    posa_a, pos_b = m.get_position()
    L=[]
    L.append(P)
    try:
        while(True):
            pos_a_new, pos_b_new = m.get_position()

            P = next_position(P, R * angle_diff(pos_a_new, posa_a), -R * angle_diff(pos_b_new, pos_b))
            posa_a = pos_a_new
            pos_b = pos_b_new
        
    finally:
        m.stop()
        m.unclock()
        with open("odometry.txt", 'w') as fp:
            for i in range(len(L)):
                for j in range(len(L[i])):
                    fp.write(str(L[i][j]))
                    if(j < len(L[i]) - 1):
                        fp.write(" ")
                if(i < len(L) - 1):
                    fp.write("\n")