import repository as repo
from input_utils import enter_name, enter_unique_index, enter_year, enter_index


def menu():
    print("--- MENU ---")
    print("1) Register new student")
    print("2) Get student data")
    print("3) Get all students data")
    print("4) Edit student data")
    print("5) Delete student")
    print("x) Exit")


def main():
    repo.load_all()
    while True:
        menu()

        choice = input(">> ")
        if choice == "1":
            new_student = [
                enter_name("name"),
                enter_name("surname"),
                enter_unique_index(),
                enter_year()
            ]
            repo.add(new_student)
        elif choice == "2":
            index = enter_index()
            student = repo.find(index)
            print_student(student)
        elif choice == "3":
            for student in repo.students:
                print_student(student)

        elif choice == "4":
            index = enter_index()
            new_student = [
                enter_name("name"),
                enter_name("surname"),
                index,
                enter_year()
            ]
            repo.update(new_student)
        elif choice == "5":
            index = enter_index()
            repo.remove(index)
        elif choice == "x":
            print("Exiting...")
            repo.save_all()
            break
        else:
            print("Invalid choice!")


def print_student(student):
    print(f"| {student[2]:11} | {student[0]:10} | {student[1]:15} | {student[3]:1} |")


if __name__ == "__main__":
    main()