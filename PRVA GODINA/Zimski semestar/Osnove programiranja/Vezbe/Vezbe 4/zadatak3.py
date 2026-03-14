if __name__ == "__main__":
    name = input("Korisnicko ime: ")
    pwd = input("Lozinka: ")
    with open("users.txt", "a") as file:
        file.write(name + "|" + pwd + "\n")