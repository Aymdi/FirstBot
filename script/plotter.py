import cv2
import numpy as np

class Plotter:
    def __init__(self, plot_width, plot_height, plot_zoom):
        self.width = plot_width
        self.height = plot_height
        self.color = (255, 0 ,0)
        self.val = []
        self.plot = np.ones((self.height, self.width, 3))*255
        self.zoom = plot_zoom

    def plot2(self, x, y, label = "plot"):
        self.val.append((x, y))
        self.show_plot(label)

    def show_plot(self, label):
        cv2.line(self.plot, (0, int(self.height/2)), (self.width, int(self.height/2)), (0,0,255), 3)
        cv2.line(self.plot, (int(self.width/2), 0), (int(self.width/2), self.height), (0,0,255), 3)
        for i in range():
            cv2.line(self.plot, (int(self.width/2 + self.zoom * i), int(self.height/2 + self.zoom * 2)), (int(self.width/2 + self.zoom * i), int(self.height/2 - self.zoom * 2)), (0,0,255), 3)
            cv2.line(self.plot, (int(self.width/2), 0), (int(self.width/2), self.height), (0,0,255), 3)

        for i in range(len(self.val)-1):
            cv2.line(self.plot, (int(self.width/2 + self.zoom*self.val[i][0]), int(self.height/2 - self.zoom*self.val[i][1])), (int(self.width/2 + self.zoom*self.val[i+1][0]), int(self.height/2 - self.zoom*self.val[i+1][1])), self.color, 3)
        cv2.imshow(label, self.plot)
        cv2.waitKey(30)
