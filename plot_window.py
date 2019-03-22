#! /usr/bin/env python3

from tkinter import Tk, Label, Button, Canvas



class DataPlot:
    """A canvas for displaying the algorithm's progress"""
    def __init__(self, master):
        self.master = master
        master.title("Plot")

        self.label = Label(master, text="Plot")
        self.label.pack()

        self.win = Canvas(self.master, width=600, height=600)
        self.win.pack()

        self.start_button = Button(master, text="Start", command=self.start)
        self.start_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def plot(self, pt):
        """Plots a Point object as 10px oval around the Point,
        and filled with the required colour."""
        x0, x1 = pt.x-5, pt.x+5
        y0, y1 = pt.y-5, pt.y+5
        self.win.create_oval(x0, y0, x1, y1, fill=pt.color)

    def start(self):
        """Possibly redundant option to start the process from
        the GUI."""
        print("Add start functionality")


class TestPoint:  # Only for testing
    """A Point class to test plotting on the DataPlot canvas"""
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

root = Tk()
plotter = DataPlot(root)
test_pts = [TestPoint(50, 50, 'green'), TestPoint(550, 550, 'red')]
for test_pt in test_pts:
    plotter.plot(test_pt)
root.mainloop()
