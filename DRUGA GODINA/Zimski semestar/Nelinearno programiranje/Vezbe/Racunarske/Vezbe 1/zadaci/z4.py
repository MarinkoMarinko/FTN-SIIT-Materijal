import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = np.arange(-5, 5.01, 0.1)
    y = np.arange(-5, 5.01, 0.1)

    X, Y = np.meshgrid(x, y)

    Z = (-20 * np.exp(-0.2 * np.sqrt((X**2 + Y**2) / 2))
        - np.exp((np.cos(2 * np.pi * X) + np.cos(2 * np.pi * Y)) / 2)
        + 20 + np.e)

    ax = plt.axes(projection="3d")
    ax.plot_surface(X, Y, Z, color="red", edgecolor="black", linewidth=0.1)

    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_zlabel("f(x1, x2)")
    ax.set_title("Ackley funkcija")

    plt.show()