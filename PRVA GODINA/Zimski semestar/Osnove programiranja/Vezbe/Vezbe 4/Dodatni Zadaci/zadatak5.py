import string
import random

def make_pass(n):
    chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = "".join(random.choice(chars) for _ in range(n))
        if check_password(password):
            return password
def check_password(password):
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    for ch in password:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif ch in string.punctuation:
            has_special = True
    return has_lower & has_upper & has_digit & has_special
if __name__ == "__main__":
    while True:
        n = eval(input("Unesite duzinu lozinke: "))
        if n < 8:
            print("Lozinka mora imati najmanje 8 karaktera. Pokusajte ponovo.")
            continue
        break
    print("Predlog dobre lozinke: ", make_pass(n))