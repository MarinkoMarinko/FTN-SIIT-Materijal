import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = np.arange(-10, 10.1, 0.1)
    y = np.sin(x) + (1 / 25) * x**2

    plt.plot(x, y, label="f(x)")
    plt.title("f(x) = sin(x) + (1 / 25) * x^2")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.legend()
    plt.grid(True)
    plt.show()