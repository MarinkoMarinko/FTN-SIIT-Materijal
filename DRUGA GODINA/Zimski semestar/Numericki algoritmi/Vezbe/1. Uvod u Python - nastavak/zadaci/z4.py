import numpy as np

if __name__ == "__main__":
    A = np.array([[1, 2],
                  [3, 4]])

    B = np.array([[0, 1],
                  [1, 0]])

    mul_1 = A @ B
    mul_2 = B @ A
    print("A * B =", mul_1)
    print("B * A =", mul_2)

    is_equal = "Jednake." if np.array_equal(mul_1, mul_2) else "Nisu jednake."
    print(is_equal)
    print("Det A:", format(np.linalg.det(A), ".2f"))