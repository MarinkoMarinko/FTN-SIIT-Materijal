import repository as repo


def enter_name(name_type):
    while True:
        name = input(f"Enter {name_type}: ")
        if name != "" and name[0].isupper():
            return name
        else:
            print(f"[ERROR]: {name_type.capitalize()} is not valid!")


def is_index_valid(index):
    try:
        major, remainder = index.split(" ")
        number, year = remainder.split("/")

        return (
            len(major) == 2
            and major.isalpha()
            and number.isdigit()
            and 1 <= len(number) <= 3
            and year.isdigit()
            and len(year) == 4
        )
    except Exception:
        return False


def is_index_unique(index):
    for student in repo.students:
        if student[2] == index:
            return False
    return True


def enter_unique_index():
    while True:
        index = input(f"Enter index number: ")
        if is_index_valid(index) and is_index_unique(index):
            return index
        else:
            print(f"[ERROR]: Index number is not valid!")


def enter_index():
    while True:
        index = input(f"Enter index number: ")
        if is_index_valid(index):
            return index
        else:
            print(f"[ERROR]: Index number is not valid!")


def enter_year():
    while True:
        year = input(f"Enter year of studies: ")
        if year in ["1", "2", "3", "4", "5"]:
            return year
        else:
            print(f"[ERROR]: Year of studies is not valid!")