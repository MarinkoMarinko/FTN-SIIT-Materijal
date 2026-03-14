from services import users
from services import scheduled


from utils import main_utils
from utils import menus


def main():
    main_utils.read_all_data()
    while True:
        menus.menu()
        choice = input("Unesite svoj izbor: ").strip()
        if choice == "1":
            users.login()                                       # 1. Prijava
        elif choice == "2":
            print("Izlaz iz aplikacije...")                     # 2. Izlaz iz aplikacije
            break
        elif choice == "3":
            scheduled.view_upcoming_flights()                   # 3. Pregled letova
        elif choice == "4":
            main_utils.flight_single_search()                   # 4. Pretraga
        elif choice == "5":
            main_utils.flight_multiple_search()                 # 5. Višekriterijumska
        elif choice == "6":
            main_utils.cheapest_flights()                       # 6. Najjeftiniji letovi
        elif choice == "7":
            main_utils.flexible_flights()                       # 7. Fleksibilni  polasci
        elif choice == "8" and not users.is_logged_in():
            users.register("customer")                          # 8. Registracija
            print("Uspešno ste se registrovali! Možete se prijaviti.")
        elif choice == "8" and users.is_logged_in():
            users.logout()                                      # 9. Odjava
        elif choice == "9" and users.has_role("customer"):
            main_utils.ticket_purchase()                        # 10. Kupovina
        elif choice == "10" and users.has_role("customer"):
            main_utils.customer_tickets()                       # 11. Moje karte
        elif choice == "11" and users.has_role("customer"):
            main_utils.customer_check_in()                      # 12. Check-in
        elif choice == "9" and users.has_role("seller"):
            main_utils.sell_ticket()                            # 13. Prodaja
        elif choice == "10" and users.has_role("seller"):
            main_utils.seller_check_in()                        # 14. Check-in
        elif choice == "11" and users.has_role("seller"):
            main_utils.ticket_update()                          # 15. Izmena karte
        elif choice == "12" and users.has_role("seller"):
            main_utils.ticket_mark_delete()                     # 16. Brisanje
        elif choice == "13" and users.has_role("seller"):
            main_utils.sold_ticket_search()                     # 17. Pretraga
        elif choice == "9" and users.has_role("manager"):
            main_utils.sold_ticket_search()                     # 17. Pretraga
        elif choice == "10" and users.has_role("manager"):
            users.register("seller")                            # 18. Novi prodavac
            print("Uspešno ste kreirali nalog prodavcu!")
        elif choice == "11" and users.has_role("manager"):
            main_utils.flight_create()                          # 19. Kreiranje leta
        elif choice == "12" and users.has_role("manager"):
            main_utils.flight_update()                          # 20. Izmena leta
        elif choice == "13" and users.has_role("manager"):
            main_utils.ticket_delete()                          # 21. Brisanje karata
        elif choice == "14" and users.has_role("manager"):
            main_utils.manager_reports()                        # 22. Izveštavanje
        else:
            print("Pogrešan izbor!")
if __name__ == "__main__":
    main()