if __name__ == "__main__":
    with open("users.txt", "r") as file:
        for line in file.readlines():
            data = line.split("|")
            print("Korisnicko ime: ", data[0])
            print("Lozinka: ", data[1])