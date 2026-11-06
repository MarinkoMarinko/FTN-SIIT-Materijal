import numpy as np


def sum_d(A):
    n, m = A.shape
    if n != m:
        raise Exception('Matrica nije kvadratna')
    return np.trace(A)


if __name__ == '__main__':
    A = np.array([[2, 1, 6, 1],
                  [1, 3, 8, 2],
                  [5, 9, 4, 3],
                  [1, 1, 8, 5]])
    print(sum_d(A))
