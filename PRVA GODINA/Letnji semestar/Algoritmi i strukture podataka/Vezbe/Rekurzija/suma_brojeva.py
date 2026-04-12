def sum_int(n):                         # O(n)
    if n <= 1:
        return n
    return n + sum_int(n - 1)


if __name__ == "__main__":
    n = 10
    print(sum_int(n))