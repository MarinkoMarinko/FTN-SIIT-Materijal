def broj_koraka(n):
    cnt = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        cnt += 1
    return cnt

if __name__ == "__main__":
    n = 27
    print("Broj koraka:", broj_koraka(n))