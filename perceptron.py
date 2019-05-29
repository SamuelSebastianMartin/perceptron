#! /usr/bin/env python3

from random import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from perceptron_class import Perceptron


def main():
    df = generate_data()
    m, c = get_line()  # y = mx + c
    df = add_label_column(df, m, c)

    p = Perceptron()
    p.df = df
    p.train()
    plot_data(df, m, c)


def generate_data():
    """
    Generates random points in a 2D plane, returning a pandas dataframe.
    """
    df = pd.DataFrame(np.random.randint(0,100,size=(100, 2))
                    , columns=['x1', 'x2'])
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


def plot_data(df, m, c):
    """
    Plots all the data points and the dividing line.
    """
    # plot points
    for x, y, label in df.itertuples(index=False):  # itertuples method.
        if label == 1:
            plt.plot(x, y, 'ro')
        else:
            plt.plot(x, y, 'go')

    # plot line: ([pt1_x, pt2_x], [pt1_y, pt2_y])
    plt.plot([0, 100], [c + (m * 0), c + (m * 100)], 'k-')

    plt.axis([0, 100, 0, 100])
    plt.show()


if __name__ == '__main__':
    main()
