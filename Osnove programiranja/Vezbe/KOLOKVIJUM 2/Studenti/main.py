import db
import inputs
def menu():
    print("\n-------- MENU --------")
    print("1) Unos novog studenta")
    print("2) Ispis jednog studenta")
    print("3) Ispis svih studenata")
    print("4) Brisanje studenta")
    print("5) Izmena studenta")
    print("x) Izlaz")
def print_student(student):
    print("Ime: ", student[0])
    print("Prezime: ", student[1])
    print("Index: ", student[2])
    print("Godina studija: ", student[3])
def print_all_students():
    for student in db.students:
        print_student(student)
        print("-------------------")
def main():
    db.load_students()
    while True:
        menu()
        choice = input("Izbor: ").strip().lower()
        match choice:
            case "1":
                print("***** Unos novog studenta *****")
                name = inputs.name_input("ime")
                surname = inputs.name_input("prezime")
                index = inputs.new_index_input()
                year = inputs.year_input()
                student = [name, surname, index, year]
                db.add_student(student)
            case "2":
                print("***** Ispis podataka o studentu *****")
                index = inputs.existing_index_input()
                student = db.find_student(index)
                print_student(student)
            case "3":
                print("***** Ispis podataka o svim studentima *****")
                print_all_students()
            case "4":
                print("***** Brisanje podataka o studentu *****")
                index = inputs.existing_index_input()
                student = db.find_student(index)
                db.delete_student(student)
            case "5":
                print("***** Izmena podataka o studentu *****")
                index = inputs.existing_index_input()
                student = db.find_student(index)
                db.update_student(student)
            case "x":
                print("Podaci sačuvani. Izlaz...")
                db.write_students()
                break
            case _:
                print("Nevažeća opcija.")

if __name__ == "__main__":
    main()