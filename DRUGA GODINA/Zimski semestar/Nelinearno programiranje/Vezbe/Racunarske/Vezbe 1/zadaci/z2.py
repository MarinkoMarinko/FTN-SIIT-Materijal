def fibo(n):
    res = []
    first, second = 0, 1
    for _ in range(n):
        res.append(first)
        first, second = second, first + second
    return res


if __name__ == "__main__":
    print(fibo(10))