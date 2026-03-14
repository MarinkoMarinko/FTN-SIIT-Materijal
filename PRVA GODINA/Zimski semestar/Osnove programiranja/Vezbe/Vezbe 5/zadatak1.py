import math
def kvJednacina(a, b, c):
    D = b*b - 4*a*c
    if D == 0:
        x = -b / (2*a)
        print(f"Jednacina ima jedno resenje i to je: {x:.2f}") 
    elif D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"Jednacina ima dva resenja i to su: {x1:.2f} i {x2:.2f}")
    else:
        print("Jednacina nema realnih resenja!") 

if __name__ == "__main__":
    a, b, c = eval(input("Unesite a, b i c: "))
    kvJednacina(a,b,c)