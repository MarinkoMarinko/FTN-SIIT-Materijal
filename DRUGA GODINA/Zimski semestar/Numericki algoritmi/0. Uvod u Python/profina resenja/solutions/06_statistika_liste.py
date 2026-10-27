def statistika(brojevi):
    '''Vraća minimum, maksimum, prosek i medijanu, bez upotrebe min(), max() i sum().'''
    minimum = brojevi[0]
    maksimum = brojevi[0]
    zbir = 0
    for x in brojevi:
        if x < minimum:
            minimum = x
        if x > maksimum:
            maksimum = x
        zbir += x
    prosek = zbir / len(brojevi)

    # medijana: sortiramo kopiju da ne bismo menjali originalnu listu
    kopija = brojevi[:]
    kopija.sort()
    n = len(kopija)
    if n % 2 == 1:
        medijana = kopija[n // 2]
    else:
        medijana = (kopija[n // 2 - 1] + kopija[n // 2]) / 2

    return minimum, maksimum, prosek, medijana


if __name__ == '__main__':
    print(statistika([4, 8, 15, 16, 23, 42]))  # (4, 42, 18.0, 15.5)
    print(statistika([7, 1, 3]))               # (1, 7, 3.666..., 3)
