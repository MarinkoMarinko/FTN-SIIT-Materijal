def zbir_parnih(n):
    '''Zbir prvih n parnih brojeva (2 + 4 + ... + 2n), pomoću while petlje.'''
    zbir = 0
    i = 1
    while i <= n:
        zbir += 2 * i  # i-ti paran broj je 2*i
        i += 1
    return zbir


if __name__ == '__main__':
    print(zbir_parnih(5))     # 30
    print(zbir_parnih(1000))  # 1001000
