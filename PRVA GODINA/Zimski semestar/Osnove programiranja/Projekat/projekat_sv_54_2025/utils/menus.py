from services import users


def menu():
    print("***** GLAVNI MENI *****")
    print("1. Prijava na sistem")
    print("2. Izlazak iz aplikacije")
    print("3. Pregled nerealizovanih letova")
    print("4. Pretraga letova")
    print("5. Višekriterijumska pretraga letova")
    print("6. Prikaz 10 najjeftinijih letova")
    print("7. Fleksibilni polasci")
    if users.logged_user == None:
        print("8. Registracija")
    else:
        print("8. Odjava sa sistema")
    if users.logged_user != None and users.logged_user["role"] == "customer":
        print("9. Kupovina karata")
        print("10. Pregled nerealizovanih karata")
        print("11. Prijava na let (check - in)")
    elif users.logged_user != None and users.logged_user["role"] == "seller":
        print("9. Prodaja karata")
        print("10. Prijava na let (check - in)")
        print("11. Izmena karte")
        print("12. Brisanje karte")
        print("13. Pretraga prodatih karata")
    elif users.logged_user != None and users.logged_user["role"] == "manager":
        print("9. Pretraga prodatih karata")
        print("10. Registracija novih prodavaca")
        print("11. Kreiranje letova")
        print("12. Izmena letova")
        print("13. Brisanje karata")
        print("14. Izveštavanje")


def search_flights_menu():
    print("***** PRETRAGA LETOVA *****")
    print("1. Po polazištu")
    print("2. Po dolazištu")
    print("3. Po datumu polaska")
    print("4. Po datumu dolaska")
    print("5. Po vremenu polaska")
    print("6. Po vremenu dolaska")
    print("7. Po prevozniku")
    print("8. Prekini pretragu")


def reports_menu():
    print("a) Lista prodatih karata za izabrani dan prodaje")
    print("b) Lista prodatih karata za izabrani dan polaska")
    print("c) Lista prodatih karata za izabrani dan prodaje i izabranog prodavca")
    print("d) Ukupan broj i cena prodatih karata za izabrani dan prodaje")
    print("e) Ukupan broj i cena prodatih karata za izabrani dan polaska")
    print("f) Ukupan broj i cena prodatih karata za izabrani dan prodaje i izabranog prodavca")
    print("g) Ukupan broj i cena prodatih karata u poslednjih 30 dana, za svakog od prodavaca")
    print("x) Izlaz")