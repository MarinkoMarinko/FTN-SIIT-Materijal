import db
def name_input(name_type):
    while True:
        try:
            name = input(f"{name_type.capitalize()}: ")
            if name.isalpha() and name[0].isupper():
                return name
            else:
                raise Exception
        except Exception:
            print(f"Greška. Unesite {name_type} u ispravnom obliku.")
def index_valid(index):
    if " " not in index or "/" not in index:
        raise Exception("Greška. Unesite index u ispravnom obliku.")
    major, remainder = index.split(" ")
    id, year = remainder.split("/")
    return (
        major.isupper() and
        len(major) == 2 and
        id.isnumeric() and
        1 <= len(id) <= 3 and
        year.isnumeric() and
        len(year) == 4
    )
def index_exists(index):
    for student in db.students:
        if student[2] == index:
            return True
    return False
def new_index_input():
    while True:
        try:
            index = input("Index: ")
            if index_valid(index):
                if index_exists(index) == False:
                    return index
                else:
                    raise Exception("Greška. Uneti index već postoji.")
            else:
                raise Exception("Greška. Unesite index u ispravnom obliku.")
        except Exception as e:
            print(e)
def existing_index_input():
    while True:
        try:
            index = input("Index: ")
            if index_valid(index):
                if index_exists(index):
                    return index
                else:
                    raise Exception("Greška. Uneti index ne postoji.")
            else:
                raise Exception("Greška. Unesite index u ispravnom obliku.")
        except Exception as e:
            print(e)
def year_input():
    while True:
        try:
            year = input("Godina studija: ")
            if year in ["1", "2", "3", "4", "5"]:
                return year
            else:
                raise Exception
        except Exception:
            print(f"Greška. Unesite godinu studija u ispravnom obliku.")
if __name__ == "__main__":
    # name_input("ime")
    # year_input()
    new_index_input()