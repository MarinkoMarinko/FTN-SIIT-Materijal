def registration(name, pwd):
    with open("prodavci.txt", "a") as file:
        file.write(name + " " + pwd + "\n")
def add_product(product, price, amount):
    with open("proizvodi.txt", "a") as file:
        file.write(product + " " + str(price) + " " + str(amount) + "\n")
def list_all_products():
    print("----- SVI PROIZVODI -----")
    with open("proizvodi.txt", "r") as file:
        for line in file.readlines():
            data = line.split()
            print("Ime proizvoda: ", data[0])
            print("Cena: ", data[1])
            print("Raspoloziva kolicina: ", data[2])
            print("--------------------------")
if __name__ == "__main__":
    name = input("Unesite ime: ")
    pwd = input("Unesite lozinku: ")
    registration(name, pwd)
    while True:
        product = input("Unesite naziv proizvoda: ").strip().lower()
        if product == "quit":
            break
        price = input("Unesite cenu proizvoda: ").strip().lower()
        if price == "quit":
            break
        amount = input("Unesite raspolozivu kolicinu proizvoda: ").strip().lower()
        if amount == "quit":
            break
        price = eval(price)
        amount = eval(amount)
        add_product(product, price, amount)
        list_all_products()