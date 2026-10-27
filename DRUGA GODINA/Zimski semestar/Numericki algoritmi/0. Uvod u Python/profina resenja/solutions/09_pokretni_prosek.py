def pokretni_prosek(niz, k):
    '''Vraća listu proseka svakih k uzastopnih elemenata niza ("rolling window").'''
    rezultat = []
    for i in range(len(niz) - k + 1):
        prozor = niz[i:i + k]
        rezultat.append(sum(prozor) / k)
    return rezultat


if __name__ == '__main__':
    print(pokretni_prosek([1, 2, 3, 4, 5, 6], 3))  # [2.0, 3.0, 4.0, 5.0]

    putnici = [112, 118, 132, 129, 121, 135]  # broj putnika, januar-jun 1949.
    print([round(p, 2) for p in pokretni_prosek(putnici, 3)])  # [120.67, 126.33, 127.33, 128.33]
