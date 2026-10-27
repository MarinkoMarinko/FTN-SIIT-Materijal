import numpy as np

def sum_d(A):
    if A.shape[0] != A.shape[1]:
        raise Exception("Greska!")
    return A.diagonal().sum()

if __name__ == "__main__":
    A = np.array([[2, 1, 6, 1],
                  [1, 3, 8, 2],
                  [5, 9, 4, 3],
                  [1, 1, 8, 5]])
    try:
        print(sum_d(A))
    except Exception as e:
        print(e)