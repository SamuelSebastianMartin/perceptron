#! /usr/bin/env/ python3

from tkinter import Tk
from plot_window import DataPlot
from point import Point

class Perceptron:
    def __init__(self):
        self.points = self.make_points()

    def make_points(self):
        points = []
        for n in range(200):
            pt = Point()
            points.append(pt)
        return points



root = Tk()
plotter = DataPlot(root)


def main():
    pcn = Perceptron()
    points = pcn.make_points()

    for pt in points:
        plotter.plot(pt)
main()

root.mainloop()
