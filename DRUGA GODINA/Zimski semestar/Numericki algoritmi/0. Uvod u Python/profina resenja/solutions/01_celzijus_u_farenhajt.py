def c_u_f(c):
    '''Pretvara stepene Celzijusa u stepene Farenhajta.'''
    return 9 / 5 * c + 32


if __name__ == '__main__':
    print(c_u_f(100))  # 212.0
    print(c_u_f(-40))  # -40.0

    # tabela za C = -10, 0, ..., 40
    print('     C |      F')
    for c in range(-10, 41, 10):
        print(f'{c:6.1f} | {c_u_f(c):6.1f}')
