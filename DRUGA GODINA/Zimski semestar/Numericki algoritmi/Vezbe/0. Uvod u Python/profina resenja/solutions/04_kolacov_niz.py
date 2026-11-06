def broj_koraka(n):
    '''Broj koraka Kolacovog niza od n do 1.'''
    koraci = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        koraci += 1
    return koraci


if __name__ == '__main__':
    print(broj_koraka(6))   # 8  (6, 3, 10, 5, 16, 8, 4, 2, 1)
    print(broj_koraka(27))  # 111
