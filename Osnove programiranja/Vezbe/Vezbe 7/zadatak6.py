def nzd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
if __name__ == "__main__":
    while True:
        a, b = eval(input("Unesite dva broja(a,b): "))
        if a >= 0 & b >= 0:
            break
        print("Pogresan unos, brojevi moraju biti pozitivni.")
    print(nzd(a,b))