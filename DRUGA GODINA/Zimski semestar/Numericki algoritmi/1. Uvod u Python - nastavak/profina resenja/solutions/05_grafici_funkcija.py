import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    x = np.arange(-2, 2.1, 0.1)

    plt.plot(x, x)
    plt.plot(x, x ** 2)
    plt.plot(x, x ** 3)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Grafici funkcija')
    plt.legend(['y = x', 'y = x²', 'y = x³'])
    plt.show()
