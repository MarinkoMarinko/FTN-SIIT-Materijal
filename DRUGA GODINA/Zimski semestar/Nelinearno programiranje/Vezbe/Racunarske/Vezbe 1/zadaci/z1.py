if __name__ == "__main__":
    n, res = 5, 1

    # for i in range(1, n + 1):
    #     res *= i

    while n > 0:
        res *= n
        n -= 1
    print(res)