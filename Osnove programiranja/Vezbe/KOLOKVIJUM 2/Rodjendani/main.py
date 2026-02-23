import db
import input_validation as iv
def menu():
    print("***** MENI *****")
    print("1. Unos novog rodjendana")
    print("2. Pretraga rodjendana")
    print("3. Odabir jednog rodjendana")
    print("4. Ispis podataka o svim rodjendanima")
    print("5. Izmena podataka o rodjendanu")
    print("6. Brisanje podataka o rodjendanu")
    print("7. Ispis rodjendana u odredjenom periodu")
    print("8. Rodjendani na danasnji dan")
    print("x. Izlaz")
def search_menu():
    print("Izaberite po čemu ćemo pretražiti rođendan:")
    print("1. Po imenu slavljenika")
    print("2. Po datumu rodjendana")
    print("x. Izlaz")
def print_birthdays(birthdays):
    print(f"{'Ime':<20} {'Datum':<15} {'Postavljen podsetnik':>10}")
    i = 1
    for birthday in birthdays:
        print(f"{i}. {birthday[0]:<20} {birthday[1]:<10} {birthday[2]:>10}")
        i += 1
def main():
    db.read_all_birthdays()
    while True:
        menu()
        choice = input("Unesite svoj izbor: ").lower()
        match choice:
            case "1":
                print("***** UNOS NOVOG RODJENDANA *****")
                name = iv.name_input()
                birthday = iv.birthday_input()
                reminder = iv.reminder_input()
                birthday = [name, birthday, reminder]
                db.birthdays.append(birthday)
            case "2":
                print("***** PRETRAGA RODJENDANA *****")
                search_menu()
                while True:
                    search_choice = input("Unesite svoj izbor: ").strip().lower()
                    if search_choice not in ["1", "2", "x"]:
                        print("Pogrešan odabir. Pokušajte ponovo")
                    elif search_choice == "x":
                        print("Izlazimo...")
                        break
                    elif search_choice == "1":
                        name = iv.name_input()
                        birthdays = db.find_birthdays(name)
                    else:
                        birthday = iv.birthday_input()
                        birthdays = db.find_birthdays(birthday)
                    print("***** ISPIS PRETRAŽENIH RODJENDANA *****")
                    print_birthdays(birthdays)
                    break
            case "3":
                print("***** ODABIR RODJENDANA *****")
                search_menu()
                while True:
                    search_choice = input("Unesite svoj izbor: ").strip().lower()
                    if search_choice not in ["1", "2", "x"]:
                        print("Pogrešan odabir. Pokušajte ponovo")
                    elif search_choice == "x":
                        print("Izlazimo...")
                        break
                    elif search_choice == "1":
                        name = iv.name_input()
                        birthdays = db.find_birthdays(name)
                    else:
                        birthday = iv.birthday_input()
                        birthdays = db.find_birthdays(birthday)
                    print("***** ISPIS PRETRAŽENIH RODJENDANA *****")
                    print_birthdays(birthdays)
                    break
                while True:
                    try:
                        selected_birthday = eval(input("Izaberite rodjendan: ").strip())
                        if selected_birthday < 1 or selected_birthday > len(birthdays):
                            print("Pogrešan odabir. Pokušajte ponovo")
                        else:
                            print("Izabrali ste rodjendan! Informacije:")
                            print(f"{birthdays[selected_birthday - 1][0]} {birthdays[selected_birthday - 1][1]} {birthdays[selected_birthday - 1][2]}")
                            break
                    except:
                        print("Pogrešan odabir. Pokušajte ponovo")
            case "4":
                print("***** ISPIS PODATAKA O SVIM RODJENDANIMA *****")
                print_birthdays(db.birthdays)
            case "5":
                print("***** ODABIR RODJENDANA *****")
                search_menu()
                while True:
                    search_choice = input("Unesite svoj izbor: ").strip().lower()
                    if search_choice not in ["1", "2", "x"]:
                        print("Pogrešan odabir. Pokušajte ponovo")
                    elif search_choice == "x":
                        print("Izlazimo...")
                        break
                    elif search_choice == "1":
                        name = iv.name_input()
                        birthdays = db.find_birthdays(name)
                    else:
                        birthday = iv.birthday_input()
                        birthdays = db.find_birthdays(birthday)
                    print("***** ISPIS PRETRAŽENIH RODJENDANA *****")
                    print_birthdays(birthdays)
                    break
                while True:
                    try:
                        selected_birthday = eval(input("Izaberite rodjendan: ").strip())
                        if selected_birthday < 1 or selected_birthday > len(birthdays):
                            print("Pogrešan odabir. Pokušajte ponovo")
                        else:
                            print("Izabrali ste rodjendan! Informacije:")
                            print(f"{birthdays[selected_birthday - 1][0]} {birthdays[selected_birthday - 1][1]} {birthdays[selected_birthday - 1][2]}")
                            break
                    except:
                        print("Pogrešan odabir. Pokušajte ponovo")
            case "6":
                pass
            case "7":
                pass
            case "8":
                pass
            case "x":
                print("Izlazimo...")
                db.write_all_birthdays()
                break
            case _:
                print("Pogrešan odabir. Pokušajte ponovo")
if __name__ == "__main__":
    main()