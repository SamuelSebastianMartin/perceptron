#! /usr/bin/env/ python3

from tkinter import Tk
from plot_window import DataPlot
from point import Point
from random import random
import time


class Perceptron:
    def __init__(self):
        self.points = self.make_points()
        self.wt_x = self.randomise_weight()
        self.wt_y = self.randomise_weight()

    def make_points(self):
        """Returns an array of 200 Point objects. The values
        of x and y are available for guessing; the actual
        'value' (1 or -1) is not available until training.
        """
        points = []
        for n in range(200):
            pt = Point()
            points.append(pt)
        return points

    def randomise_weight(self):
        """A one-time function to set random initial values"""
        wt = random()
        if wt > 0.5:
            return 1
        else:
            return -1

    def guess(self, x, y):
        """The perceptron makes an 'educated' guess for 'value'
        based on the Point co-ordinates (x, y) and the 'weights',
        which are modified during 'training'
        """
        addition = (x * self.wt_x) + (y * self.wt_y)
        if addition >= 0:
            return 1
        else:
            return -1

    def train(self):
        learn_rate = 0.1
        for pt in self.points:
#            time.sleep(0.5)
            guess = self.guess(pt.x, pt.y)
            error = pt.value - guess
            if guess == pt.value:
                pt.color = 'green'
            else:
                pt.color = 'red'
            plotter.plot(pt)
            #  'teach' weights.
            self.wt_x = self.wt_x * error * learn_rate
            self.wt_y = self.wt_y * error * learn_rate



root = Tk()
plotter = DataPlot(root)


def main():
    pcn = Perceptron()
    points = pcn.make_points()
    for pt in points:
        plotter.plot(pt)
    for n in range(10):
        input('click to continue')
        pcn.train()
main()

root.mainloop()
