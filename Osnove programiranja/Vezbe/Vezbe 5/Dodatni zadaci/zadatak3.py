# Digitron
def input_numbers():
    a = 0
    b = 0
    while True:
        try:
            a = eval(input("Unesite prvi broj: "))
            b = eval(input("Unesite drugi broj: "))
        except ValueError:
            print("Pogresan unos!")
            continue
        break
    return a, b
def print_menu():
    print("DOSTUPNE OPERACIJE")
    print("=======================================")
    print("Sabiranje: +")
    print("Oduzimanje: -")
    print("Mnozenje: *")
    print("Deljenje: /")
    print("Celobrojno deljenje: //")
    print("Stepenovanje: **")
    print("=======================================")
def calculator(a, b):
    while True:
        print_menu()
        operator = input("Unesite znak: ").strip()
        if operator not in ['+', '-', '*', '/', '//', '**']:
            print("Morate uneti ispravan znak!")
        else:
            print(f"Rezultat: {a} {operator} {b} = {operation(a, b, operator)}")
        answer = input("Ponovo? y ili n: ").lower()
        if answer == "n":
            break
def operation(a, b, operator):
    try:
        if a < 0 and -1 < b < 1 and b != 0 and operator == "**":
            raise Exception("Ne moze se odrediti koren negativnog broja!")
        result = eval(str(a) + operator + str(b))
    except ZeroDivisionError:
        return "Ne sme se deliti nulom!"
    except ValueError:
        return "Greska pri racunanju!"
    except Exception as e:
        return str(e)
    return result
if __name__ == "__main__":
    a, b = input_numbers()
    calculator(a, b)