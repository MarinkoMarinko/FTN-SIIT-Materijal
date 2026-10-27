def je_palindrom(tekst):
    '''Proverava da li se tekst čita isto unapred i unazad (bez obzira na velika slova i razmake).'''
    tekst = tekst.lower().replace(' ', '')
    return tekst == tekst[::-1]


if __name__ == '__main__':
    for tekst in ['Ana voli Milovana', 'Kapak', 'Python']:
        print(f'{tekst!r} -> {je_palindrom(tekst)}')  # True, True, False
