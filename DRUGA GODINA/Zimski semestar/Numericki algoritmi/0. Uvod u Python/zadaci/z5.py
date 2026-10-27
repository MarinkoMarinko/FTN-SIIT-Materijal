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

    def povrsina(self):
        return super().povrsina()

    def obim(self):
        return super().obim()


if __name__ == "__main__":
    p1 = Pravougaonik(3, 4)
    k = Kvadrat(5)
    p2 = Pravougaonik(2, 10)

    print(f"Pravougaonik 1: Povrsina: {p1.povrsina()}, Obim: {p1.obim()}")
    print(f"Pravougaonik 2: Povrsina: {p2.povrsina()}, Obim: {p2.obim()}")
    print(f"Kvadrat: Povrsina: {k.povrsina()}, Obim: {k.obim()}")

    if p1.povrsina() >= k.povrsina() and p1.povrsina() >= p2.povrsina():
        najveci = p1
    elif k.povrsina() >= p2.povrsina():
        najveci = k
    else:
        najveci = p2

    print("Najveću površinu ima:", type(najveci).__name__)
