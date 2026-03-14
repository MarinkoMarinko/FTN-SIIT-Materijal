if __name__ == "__main__":
    while True:
        n = eval(input("Unesite broj: "))
        if n >= 0:
            break
        print("Broj ne sme biti negativan: ")
    divisitors = []
    divisitors = [i for i in range(1, n + 1) if n % i == 0]
    print(divisitors)