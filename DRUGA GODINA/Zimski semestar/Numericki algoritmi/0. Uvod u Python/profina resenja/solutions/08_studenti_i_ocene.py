studenti = {"Ana": [10, 9, 8], "Marko": [6, 7, 6], "Ivana": [9, 10, 10], "Jovan": [7, 8, 6]}


def prosek(ocene):
    return sum(ocene) / len(ocene)


if __name__ == '__main__':
    # rečnik student -> prosek
    proseci = {}
    for ime, ocene in studenti.items():
        proseci[ime] = round(prosek(ocene), 2)
    print(proseci)  # {'Ana': 9.0, 'Marko': 6.33, 'Ivana': 9.67, 'Jovan': 7.0}

    # student sa najboljim prosekom
    najbolji, najbolji_prosek = '', 0
    for ime, p in proseci.items():
        if p > najbolji_prosek:
            najbolji, najbolji_prosek = ime, p
    print('Najbolji prosek:', najbolji, najbolji_prosek)  # Ivana 9.67

    # studenti sa prosekom bar 8
    dobri = [ime for ime, p in proseci.items() if p >= 8]
    print(dobri)  # ['Ana', 'Ivana']
