if __name__ == "__main__":
    unos = input("Unesite frazu: ").strip()
    niz = unos.title().split()
    akronim = ""
    for i in niz:
        akronim += i[0]
    print("Akronim za unetu frazu je: " + akronim)