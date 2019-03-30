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
        for n in range(6):
            pt = Point()
            points.append(pt)
        return points

    def randomise_weight(self):
        """A one-time function to set random initial values"""
        rnd = random()
        weight = (rnd - 0.5) * 2  # (-1, 1]
        return weight

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
            guess = self.guess(pt.x, pt.y)
            error = pt.value - guess
            if error == 0:
                print('green', pt.value, guess)
                pt.color = 'green'
            else:
                pt.color = 'red'
                print('red', pt.value, guess)

                self.wt_x = self.wt_x - (error * learn_rate * pt.x)
                self.wt_y = self.wt_y - (error * learn_rate * pt.y)

root = Tk()
plotter = DataPlot(root)


def main():
    pcn = Perceptron()
    print([pt.x for pt in pcn.points])  #
    for pt in pcn.points:
        plotter.plot(pt)

    print()
    for n in range(2):
        wait_null = input('click to contiue')
        pcn.train()
        print([pt.color for pt in pcn.points], pcn.wt_x, pcn.wt_y)
        for pt in pcn.points:
            plotter.plot(pt)
#        print(pcn.wt_x, pcn.wt_y)
main()

root.mainloop()
