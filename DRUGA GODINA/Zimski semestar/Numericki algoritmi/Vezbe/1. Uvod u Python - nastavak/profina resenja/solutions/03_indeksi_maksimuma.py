import numpy as np


def indeksi_maksimuma(A):
    return np.argmax(A, axis=1)


if __name__ == '__main__':
    A = np.array([[-2, 5, 3],
                  [-1, -1, 0],
                  [-1, -5, -3]])
    print(indeksi_maksimuma(A))
