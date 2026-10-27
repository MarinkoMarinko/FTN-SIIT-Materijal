def zbir_parnih(n):
    s = 0
    for i in range(n + 1):
        s += i if i % 2 == 0 else 0
    return s

if __name__ == "__main__":
    n = 5
    print(zbir_parnih(n))