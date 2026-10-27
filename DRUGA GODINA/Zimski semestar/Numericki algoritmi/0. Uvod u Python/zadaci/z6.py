def statistika(brojevi):
    najmanji = najveci = brojevi[0]
    zbir = 0

    for broj in brojevi:
        if broj < najmanji:
            najmanji = broj
        if broj > najveci:
            najveci = broj
        zbir += broj

    prosek = zbir / len(brojevi)

    brojevi = sorted(brojevi)
    n = len(brojevi)

    if n % 2 == 0:
        medijana = (brojevi[n // 2 - 1] + brojevi[n // 2]) / 2
    else:
        medijana = brojevi[n // 2]

    return najmanji, najveci, prosek, medijana


if __name__ == "__main__":
    print(statistika([4, 8, 15, 16, 23, 42]))