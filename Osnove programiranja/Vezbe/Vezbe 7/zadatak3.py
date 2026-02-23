def sirakuza(x):
    nums = [x]
    while x != 1: 
        if x % 2 == 0:
            x /= 2
        else:
            x = x*3 + 1
        nums.append(x)
    return nums
if __name__ == "__main__":
    while True:
        n = eval(input("Unesite broj: "))
        if n > 0:
            break
        print("Pogresan unos, unesite broj veci od 0.")
    print(sirakuza(n))