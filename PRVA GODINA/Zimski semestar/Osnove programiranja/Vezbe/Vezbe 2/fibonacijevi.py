# 1 1 2 3 5 8 13 ...

if __name__ == "__main__":
    n = 0;
    while n <= 0:
        n = eval(input("Unesite broj clanova Fibonacijevog niza: "))
    x = 1
    y = 1
    ispis = ""
    for i in range(n): 
        ispis = ispis + str(x) + " "
        temp = y
        y = x + y
        x = temp
    print(ispis)