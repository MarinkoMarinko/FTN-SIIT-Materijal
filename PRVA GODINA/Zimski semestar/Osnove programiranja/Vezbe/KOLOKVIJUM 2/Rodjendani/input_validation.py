def valid_name(name):
    return (
        len(name) > 0 and 
        name.isalpha() and
        name[0].isupper()
    )
def name_input():
    while True:
        name = input("Unesite ime: ").strip()
        if valid_name(name):
            return name
        else:
            print("Pogrešan unos imena. Pokušajte ponovo.")
def birthday_valid(birthday):
    day, month, year = birthday.split(".")
    return (
        1 <= len(day) <= 2 and
        day.isnumeric() and
        1 <= len(month) <= 2 and
        month.isnumeric() and
        len(year) == 4 and
        year.isnumeric() and
        1 <= eval(day) <= 31 and
        1 <= eval(month) <= 12
    )
def birthday_input():
    while True:
        try:
            birthday = input("Unesite rodjendan(dd.mm.yyyy): ").strip()
            if birthday_valid(birthday):
                return birthday
            else:
                print("Pogrešan unos datuma. Pokušajte ponovo.")
        except Exception:
            print("Pogrešan unos datuma. Pokušajte ponovo.")
def reminder_input():
    while True:
        reminder = input("Da li zelite da postavite podsetnik? (da/ne): ").strip().lower()
        if reminder in ["da", "ne"]:
            return reminder
        else:
            print("Pogrešan unos. Pokušajte ponovo.")

if __name__ == "__main__":
    name_input()
    birthday_input()
    reminder_input()