#! /usr/bin/env/ python3

from random import random


class Point:
    """A 'Point' object can be drawn on the tkinter canvas.
    Points instantiate themselves with random co-ordinates,
    and also hold the correct 'value', which the perceptron
    will guess at.
    """
    def __init__(self):
        x_range=600
        y_range=600
        self.x = int(random() * x_range)
        self.y = int(random() * y_range)
        self.value = self.get_value()
        self.color = self.get_color()

    def get_value(self):
        if self.x >= self.y:
            return 1
        else:
            return -1

    def get_color(self):
        if self.value == 1:
            return 'black'
        elif self.value == -1:
            return None
        else:
            raise Exception('self.value in not 1 or -1')
