def prostBroj(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def prost_list(n):
    list = []
    for i in range(1, n):
        if prostBroj(i):
            list.append(i)
    return list

if __name__ == "__main__":
    while True:
        n = eval(input("Unesite broj: "))
        if n > 0:
            break
        print("Pogresan unos, broj mora biti veci od 0.")
    print(prost_list(n))