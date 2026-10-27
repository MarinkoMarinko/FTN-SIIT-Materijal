class Pravougaonik:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def povrsina(self):
        return self.a * self.b

    def obim(self):
        return 2 * (self.a + self.b)


class Kvadrat(Pravougaonik):
    def __init__(self, a):
        super().__init__(a, a)


if __name__ == '__main__':
    oblici = [Pravougaonik(3, 4), Kvadrat(5), Pravougaonik(2, 10)]

    for oblik in oblici:
        print(f'{type(oblik).__name__} {oblik.a}x{oblik.b}: površina = {oblik.povrsina()}, obim = {oblik.obim()}')

    # oblik sa najvećom površinom
    najveci = oblici[0]
    for oblik in oblici:
        if oblik.povrsina() > najveci.povrsina():
            najveci = oblik
    print(f'Najveću površinu ima {type(najveci).__name__} {najveci.a}x{najveci.b}: {najveci.povrsina()}')
