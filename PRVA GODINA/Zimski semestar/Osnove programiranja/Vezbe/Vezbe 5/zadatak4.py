def citanjeIzFajla(file, delimiter):
    list = []
    with open(file + ".txt", "r") as file:
        for line in file.readlines():
            inner_list = line.strip().split(delimiter)
            list.append(inner_list)
    print(list)
def upisUFajl(name, surname, file, delimiter):
    with open(file + ".txt", "a") as file_in:
       file_in.write(name + delimiter + surname + "\n")
    citanjeIzFajla(file, delimiter)
if __name__ == "__main__":
    file = input("U koji fajl upisujemo? ").lower()
    delimiter = input("Koji delimiter? ")
    name = input("Unesite ime: ")
    surname = input("Unesite prezime: ")
    upisUFajl(name, surname, file, delimiter)