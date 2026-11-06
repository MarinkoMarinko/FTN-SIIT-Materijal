import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    x = np.arange(-2, 2, 0.1)
    y_line = x
    y_square = x ** 2
    y_cube = x ** 3

    plt.plot(x, y_line, label = "y = x")
    plt.plot(x, y_square, label = "y = x^2")
    plt.plot(x, y_cube, label = "y = x^3")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Grafici funkcija")
    plt.legend()
    plt.grid()

    plt.show()