def ucestalost(tekst):
    '''Vraća rečnik: reč -> broj pojavljivanja (bez obzira na velika slova).'''
    recnik = {}
    for rec in tekst.lower().split():
        recnik[rec] = recnik.get(rec, 0) + 1
    return recnik


if __name__ == '__main__':
    u = ucestalost('Jabuka kruška jabuka šljiva kruška jabuka')
    print(u)  # {'jabuka': 3, 'kruška': 2, 'šljiva': 1}

    # dve najčešće reči
    sortirano = sorted(u.items(), key=lambda par: par[1], reverse=True)
    for rec, broj in sortirano[:2]:
        print(f'{rec}: {broj}')  # jabuka: 3, kruška: 2
