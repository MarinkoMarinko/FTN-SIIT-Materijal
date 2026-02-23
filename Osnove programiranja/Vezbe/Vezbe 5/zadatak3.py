def citanjeIzFajla(file, delimiter):
    list = []
    with open(file + ".txt", "r") as file:
        for line in file.readlines():
            inner_list = line.strip().split(delimiter)
            list.append(inner_list)
    return list

if __name__ == "__main__":
    file = input("Koji fajl citamo? ").lower()
    delimiter = input("Koji delimiter? ")
    print(citanjeIzFajla(file, delimiter))