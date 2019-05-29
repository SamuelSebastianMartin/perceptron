#! /usr/bin/env python3

import pandas as pd
import numpy as np
from random import random


class Perceptron:
    def __init__(self):
        self.w1 = random()
        self.w2 = random()
        self.b = random()
        self.x1 = 0
        self.x2 = 0
        self.rate = 0.1

    def predict(self):
        """
        Taking imputs x1 w1 + x2 w2 + b, this returns either 1 or 0
        depending on the threshold: <= 0
        """
        guess = self.x1 * self.w1 + self.x2 * self.w2 + self.b
        if guess < 0:
            return 0
        else:
            return 1
        return result


    def update_weights(self):
        scalar = self.rate * (self.label - self.predict())
        self.w1 = self.w1 + scalar * self.x1
        self.w2 = self.w2 + scalar * self.x2
        self.b = self.b + scalar * 1 # implicit value is 1, b is the weight.


def test():
    # instantiate perceptron
    p = Perceptron()


if __name__ == '__main__':
    test()
