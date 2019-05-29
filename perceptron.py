#! /usr/bin/env python3
from random import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from perceptron_class import Perceptron


def main():
    # Get line to calculate label (the line that will be guessed).
    m, c = get_line()  # y = mx + c

    # Get learning data            | x1 | x2 | label |
    learning_df = generate_data()
    learning_df = add_label_column(learning_df, m, c)

    # Create and train perceptron
    p = Perceptron()
    train_perceptron(p, learning_df)

    # Get new data for testing     | x1 | x2 | label |
    test_df = generate_data()
    test_df = add_label_column(test_df, m, c)  # to find error

    # Test the perceptron on the new data
    test_df = add_guess_colunm(test_df, p)

    # plot results
    plot_data(test_df, m, c)  # change to df (not learning)


def generate_data():
    """
    Generates random points in a 2D plane, returning a pandas dataframe.
    """
    df = pd.DataFrame(np.random.randint(0, 100, size=(9000, 2)),
                      columns=['x1', 'x2'])
    return df


def get_line():
    """
    Generates random slope, -5 < m < 5, and intercept, 20 < c < 80,
    for the line y = mx + c
    """
    m = (random() * 10) - 5
    c = (random() * 60) + 20
    return m, c


def add_label_column(df, m, c):
    """Adds a column with the expected answer (1 or 0).
    """
    label = []

    for index, row in df.iterrows():
        x = (row['x1'])
        y = (row['x2'])
        if y >= m * x + c:
            label.append(1)
        else:
            label.append(0)
    df['label'] = label
    return df


def train_perceptron(p, test_df):
    for x1, x2, label in test_df.itertuples(index=False):
        p.x1 = x1
        p.x2 = x2
        p.label = label
        p.update_weights()


def add_guess_colunm(df, p):
    guesses = []
    for x1, x2, label in df.itertuples(index=False):
        p.x1 = x1
        p.x2 = x2
        p.label = label
        guess = p.predict()
        guesses.append(guess)
    df['guess'] = guesses
    return df


def plot_data(df, m, c):
    """
    Plots all the data points and the dividing line.
    """
    # plot points
    for x, y, label, guess in df.itertuples(index=False):  # itertuples method.
        if label == 1 and guess == 1:  # good
            plt.plot(x, y, 'go')
        elif label == 1 and guess == 0: # bad
            plt.plot(x, y, 'rs')
        elif label == 0 and guess == 0: # good
            plt.plot(x, y, 'gs')
        elif label == 0 and guess == 1: # bad
            plt.plot(x, y, 'rs')

    # plot line: ([pt1_x, pt2_x], [pt1_y, pt2_y])
    plt.plot([0, 100], [c + (m * 0), c + (m * 100)], 'k-')

    plt.axis([0, 100, 0, 100])
    plt.show()


if __name__ == '__main__':
    main()
