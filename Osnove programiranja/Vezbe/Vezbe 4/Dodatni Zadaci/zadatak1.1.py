def read_names():
    names = {}
    with open("names.txt", "r") as file:
        for line in file:
            name = line.strip()
            if name in names:
                names[name] += 1
            else:
                names[name] = 1
    return names
def max(names):
    max_name = ""
    max_count = 0
    for name, count in names.items():
        if count > max_count:
            max_name = name
            max_count = count
    return max_name, max_count
if __name__ == "__main__":
    name = input("Unesite ime: ")
    names_dictionary = read_names()
    if name in names_dictionary:
        print(f"Ime {name} se pojavljuje {names_dictionary[name]} puta.")
    else:
        print(f"Ime {name} se ne pojavljuje u fajlu.")
    max_name, max_count = max(names_dictionary)
    print(f"Najvise pojavljivanja ima: {max_name}, {max_count} pojavljivanja")