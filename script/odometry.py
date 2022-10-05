from doctest import script_from_examples
import numpy as np
import matplotlib.pyplot as plt
import cv2
import motor
L = 16.5
R = 2.5

class Plotter:
    def __init__(self, plot_width, plot_height):
        self.width = plot_width
        self.height = plot_height
        self.color = (255, 0 ,0)
        self.val = []
        self.plot = np.ones((self.height, self.width, 3))*255

    def plot2(self, x, y, label = "plot"):
        self.val.append((x, y))
        self.show_plot(label)

    def show_plot(self, label):
        cv2.line(self.plot, (0, int(self.height/2)), (self.width, int(self.height/2)), (0,0,255), 3)
        for i in range(len(self.val)-1):
            cv2.line(self.plot, (int(self.width/2 + self.val[i][0]), int(self.height/2 - self.val[i][1])), (int(self.width/2 + self.val[i+1][0]), int(self.height/2 - self.val[i+1][1])), self.color, 3)
        cv2.imshow(label, self.plot)
        cv2.waitKey(30)

def add_position(P, va, vb):
    x, y, o = P[len(P) - 1]
    if(va - vb == 0):
        on = o
        xn = x + va * np.cos(o)
        yn = y + va * np.sin(o)
        P.append(np.array([xn, yn, on]))
    else:
        OG = L/2 * (va + vb)/(vb - va)
        do = (vb - va) / L
        xn = x + OG * (np.sin(o + do) - np.sin(o))
        yn = y - OG * (np.cos(o + do) - np.cos(o))
        on = o + do
        P.append(np.array([xn, yn, on]))

def angle_diff(a,b):
    d = a - b
    if(d>np.pi):
        d -= 2*np.pi
    return d

if __name__=="__main__":
    P = [np.array([0, 0, 0])]
    plotter = Plotter(1000, 1000)
    m = motor()
    pa, pb = m.get_position()
    while(True):
        pan, pbn = m.get_position()

        plotter.plot2(P[len(P) - 1][0], P[len(P) - 1][1])
        add_position(P, R * angle_diff(pan, pa), R * angle_diff(pbn - pb))
        pa = pan
        pb = pbn