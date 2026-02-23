books = []

def load_all(filename="books.txt"):
    global books
    books = []

    with open(filename, "r") as file:
        for line in file:
            books.append(line.strip("\n").split("|"))


def save_all(filename="books.txt"):
    with open(filename, "w") as file:
        for book in books:
            file.write("|".join(book) + "\n") # 111|111|111|...|aa\n


def find_by_isbn(isbn):
    for book in books:
        if book[0] == isbn:
            return book
    return None


def add(book):
    books.append(book)


def remove(isbn):
    for book in books:
        if book[0] == isbn:
            books.remove(book)
            return


def update(book):
    isbn = book[0]
    for i in range(len(books)):
        if books[i][0] == isbn:
            books[i] = book


def find_all_by_book_name(name):
    # found = []
    # for book in books:
    #     if name.lower() in book[1].lower():
    #         found.append(book)
    # return found

    return [book for book in books if name.lower() in book[1].lower()]

def find_all_by_authors_name(name):
    # found = []
    # for book in books:
    #     fullname = f"{book[2]} {book[3]}"
    #     if name.lower() in fullname.lower():
    #         found.append(book)
    # return found

    return [book for book in books if name.lower() in f"{book[2]} {book[3]}".lower()]


def find_all_published_at(year):
    return [book for book in books if book[4] == year]


def find_all_published_past(year):
    return [book for book in books if book[4] >= year]


def get_total_number_of_books():
    # total = 0
    # for book in books:
    #     total += int(book[5])
    # return total
    return sum(int(book[5]) for book in books)


if __name__ == "__main__":
    load_all()
    print(books)
    save_all()