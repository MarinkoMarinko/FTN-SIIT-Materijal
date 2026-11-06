import numpy as np


if __name__ == '__main__':
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[0, 1], [1, 0]])

    AB = A @ B
    BA = B @ A
    print('A @ B =\n', AB)
    print('B @ A =\n', BA)
    print('Jednake:', np.array_equal(AB, BA))
    print('det(A) =', np.linalg.det(A))
