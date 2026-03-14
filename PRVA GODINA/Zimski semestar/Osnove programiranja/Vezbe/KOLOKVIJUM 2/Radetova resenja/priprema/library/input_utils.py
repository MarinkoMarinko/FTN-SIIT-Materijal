import repository as repo


def enter_name(name_type):
    while True:
        name = input(f"Enter {name_type}: ")
        if name != "" and name[0].isupper():
            return name
        else:
            print(f"[ERROR]: {name_type.capitalize()} is not valid!")


def enter_isbn():
    while True:
        isbn = input(f"Enter ISBN: ")
        if isbn != "" and len(isbn) == 3:
            return isbn
        else:
            print(f"[ERROR]: ISBN is not valid!")


def is_unique_isbn(isbn):
    # Ako funkcija find_by_isbn ne pronadje knjigu sa odgovarajucim ISBN-om vratice None
    # To znaci da prosledjeni ISBN trenutno ne postoji u kolekciji
    return repo.find_by_isbn(isbn) is None


def enter_unique_isbn():
    while True:
        isbn = input(f"Enter ISBN: ")
        if isbn != "" and len(isbn) == 3 and is_unique_isbn(isbn):
            return isbn
        else:
            print(f"[ERROR]: ISBN is not valid!")


def enter_year():
    while True:
        year = input(f"Enter year: ")
        if year != "" and year.isdigit() and int(year) > 0:
            return year
        else:
            print(f"[ERROR]: Year is not valid!")


def enter_count():
    while True:
        count = input(f"Enter count: ")
        if count != "" and count.isdigit() and int(count) >= 0:
            return count
        else:
            print(f"[ERROR]: Count is not valid!")