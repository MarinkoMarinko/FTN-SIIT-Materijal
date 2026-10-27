import numpy as np

def sum_greater(A):
    return np.sum(A[A > np.mean(A)])

if __name__ == "__main__":
    A = np.array([
    [ 2, 1, 2,  6, 8, 1, -2],
    [15, 4, 7, 18, 4, 0, 12],
    [11, 6, 9, -1, 4, 8,  0],
    [ 2, 8, 6,  8, 1, 8,  7]])

    print(sum_greater(A))