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
        self.df = pd.DataFrame(np.random.randint(0,1,
                    size=(1, 3)), columns=['x1', 'x2', 'label'])

    def predict(self):
        """
        Taking imputs x1 w1 + x2 w2 + b, this returns either 1 or 0
        depending on the threshold: <= 0
        """
        guess = self.x1 * self.w1 + self.x2 * self.w2 + self.b
        if guess <= 0:
            return 0
        else:
            return 1


    def train(self):
        for x1, x2, label in self.df.itertuples(index=False):
            self.x1 = x1
            self.x2 = x2
            self.label = label
        self.update_weights()


    def update_weights(self):
        scalar = self.rate * (self.df['label'] - self.predict())
        self.w1 = self.w1 + scalar * self.x1
        self.w2 = self.w2 + scalar * self.x2
        self.b = self.b + scalar * 1 # implicit value is 1, b is the weight.


def test():
    # make test data
    df = pd.DataFrame(np.random.randint(0,100,size=(10, 2))
                    , columns=['x1', 'x2'])
    labels = []
    for x1, x2 in df.itertuples(index=False):
        if x1 <= 50:
            labels.append(0)
        else:
            labels.append(1)
    df['label'] = labels

    # make instantiate perceptron
    p = Perceptron()
    # feed it the test data
    p.df = df
    print(p.x1, p.w2, p.b)
    p.train()
    print(p.x1, p.w2, p.b)


if __name__ == '__main__':
    test()
