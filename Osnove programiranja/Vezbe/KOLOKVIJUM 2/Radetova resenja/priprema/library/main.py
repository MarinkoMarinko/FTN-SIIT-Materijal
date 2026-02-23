import repository as repo
import input_utils as iu


def menu():
    print("--- MENU ---")
    print("1) Register new book")
    print("2) Find book by ISBN")
    print("3) Get all books data")
    print("4) Update book data")
    print("5) Delete book")
    print("6) Find books by book name")
    print("7) Find books by author name")
    print("8) Find books by publication year")
    print("9) Find books past certain year")
    print("x) Exit")


def main():
    repo.load_all()
    while True:
        menu()

        choice = input(">> ")
        if choice == "1":
            new_book = [
                iu.enter_unique_isbn(),
                iu.enter_name("book name"),
                iu.enter_name("author name"),
                iu.enter_name("author surname"),
                iu.enter_year(),
                iu.enter_count()
            ]
            repo.add(new_book)
        elif choice == "2":
            isbn = iu.enter_isbn()
            print_one(repo.find_by_isbn(isbn))
        elif choice == "3":
            print_many(repo.books)
        elif choice == "4":
            new_book = [
                iu.enter_isbn(),
                iu.enter_name("book name"),
                iu.enter_name("author name"),
                iu.enter_name("author surname"),
                iu.enter_year(),
                iu.enter_count()
            ]
            repo.update(new_book)
        elif choice == "5":
            isbn = iu.enter_isbn()
            repo.remove(isbn)
        elif choice == "6":
            name = iu.enter_name("book name")
            print_many(repo.find_all_by_book_name(name))
        elif choice == "7":
            name = iu.enter_name("author name")
            print_many(repo.find_all_by_authors_name(name))
        elif choice == "8":
            year = iu.enter_year()
            print_many(repo.find_all_published_at(year))
        elif choice == "9":
            year = iu.enter_year()
            print_many(repo.find_all_published_past(year))
        elif choice == "x":
            print("Exiting...")
            repo.save_all()
            break
        else:
            print("Invalid choice!")

# Formatira i ispisuje jednu knjigu
def print_one(book):
    print(f"| {book[0]:3} | {book[1]:20} | {book[2]:10} | {book[3]:14} | {book[4]:>4} | {book[5]:>5} |")

# Formatira i ispisuje listu knjiga
def print_many(books):
    for book in books:
        print_one(book)


if __name__ == "__main__":
    main()