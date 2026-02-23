def prostBroj(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    while True:
        n = eval(input("Unesite broj: "))
        if n > 0:
            break
        print("Pogresan unos, broj mora biti veci od 0.")
    print(prostBroj(n))