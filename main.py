import matplotlib.pyplot as plt
import numpy as np

from os.path import join
from os import getcwd

X = []
y = []

current_class = 1

colors = [
    "red",
    "blue",
    "green",
    "black",
    "brown",
    "magenta",
    "cyan",
    "orange",
    "teal",
]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_title("Press keys 1-9 to select class")

def mouse_listener(event):
    X.append([event.xdata, event.ydata])
    y.append(current_class)

    plt.plot(event.xdata, event.ydata, color=colors[current_class-1], marker="o")
    fig.canvas.draw()


def key_listener(event):
    if int(event.key) in list(range(1, 10)):
        global current_class
        current_class = int(event.key)

fig.canvas.mpl_connect('button_press_event', mouse_listener)
fig.canvas.mpl_connect('key_press_event', key_listener)
plt.show()

X = np.array(X).reshape(-1, 2)
y = np.array(y).astype(np.int64).reshape(-1) - 1

ds_name = input("Name of dataset (default: 'toy'):") or "toy"

ds_loc = input("Store dataset to (absolute path) (default: current dir):") or getcwd()

np.savetxt(join(ds_loc, ds_name+"_X.csv"), X, delimiter=",")
np.savetxt(join(ds_loc, ds_name+"_y.csv"), y, delimiter=",")
