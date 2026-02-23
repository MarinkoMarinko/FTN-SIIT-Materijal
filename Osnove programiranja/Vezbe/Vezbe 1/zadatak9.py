# chaos.py
# Program ilustruje haoticno ponasanje :)

if __name__=="__main__":
    print("Ovaj program ilustruje haoticno ponasanje")
    x = eval(input("Unesite broj izmedju 0 i 1: "))
    y = eval(input("Unesite broj izmedju 0 i 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1-y)
        print(x, y)