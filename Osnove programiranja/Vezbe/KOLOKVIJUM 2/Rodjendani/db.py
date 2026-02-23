birthdays = []

def read_all_birthdays(filename="birthdays.txt"):
    global birthdays
    birthdays = []
    with open(filename) as file:
        for line in file:
            birthdays.append(line.strip().split(" "))
def write_all_birthdays(filename="birthdays.txt"):
    global birthdays
    with open(filename, "w") as file:
        file.write("\n".join(" ".join(birthday) for birthday in birthdays))
def find_birthdays(search_param):
    if "." not in search_param:
        return [birthday for birthday in birthdays if birthday[0] == search_param]
    else:
        return [birthday for birthday in birthdays if birthday[1] == search_param]
if __name__ == "__main__":
    read_all_birthdays()
    #print(birthdays)
    #write_all_birthdays("test.txt")
    print(find_birthdays("Marko"))