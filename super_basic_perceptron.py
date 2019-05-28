#! /usr/bin/env python3

"""
This is  very basic perceptron, worked out from first principles,
and with little regard for the tutorials etc.. Therefore, it is
very possible that I am barking up the wrong tree, but it will at
least be my tree!

The engine decides whether some value on the numberline is either
a pass or fail, the exact pass number/grade is imputted by the
user, and is never passed to the perceptron. Test data is generated
in a separate function, and used to train the perceptron.

Finally, there a Q and A interactive session, where the user can
feed numbers to the perceptron, and it will yield 'pass' or 'fail'
"""

from random import random


class Perceptron:
    """
    This Perceptron trains on paired data (x, ans), showing a random 
    variable, X, and the know answer to that variable, 'ans'.
    After training, the get_guess method will yeild a guessed answer
    for any imput value of x.
    """
    def __init__(self):
        self.x = 0    # Raw imput.
        self.ans = 0  # Obtained from training data.
        self.w = 0    # Weight.
        self.learn_rate = 0.1

    def get_guess(self):
        if (self.x * self.w) < 1:
            return 0
        else:
            return 1

    def train(self):
        self.w = self.learn_rate * (self.ans - self.get_guess()) + self.w


def main():
    threshold = get_threshold()
    trainin_data = get_training_data(threshold)
    P = Perceptron()
    train_perceptron(P, trainin_data)
    test_perceptron_interactive(P)


def get_threshold():
    threshold = float(input("\nWhat pass mark do you want, out of 10?  "))
    if threshold > 10 or threshold < 0:
        print("\nThe threshold must be between 0 and 10")
        get_threshold()
    return threshold


def get_training_data(threshold):
    data = []
    for i in range(200000):
        x = random()*10
        if x >= threshold:
            ans = 1
        else:
            ans = 0
        data.append((x, ans))
    return data


def train_perceptron(P, trainin_data):
    for datum in trainin_data:
        P.x = datum[0]
        P.ans = datum[1]
        P.train()


def test_perceptron_interactive(P):
    for n in range(5):
        trial = float(input("\nGive the perceptron a grade to assess:  "))
        P.x = trial
        if P.get_guess() == 1:
            print("PASS")
        else:
            print("FAIL")


if __name__ == '__main__':
    main()
