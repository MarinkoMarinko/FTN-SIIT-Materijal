from services import users
from services import flights
from services import scheduled
from services import airplanes
from services import airports
from services import tickets


from utils import inputs
from utils import menus


def read_all_data():
    users.read_users("./data/users.csv")
    flights.read_flights("./data/flights.csv")
    scheduled.read_scheduled("./data/scheduled.csv")
    airplanes.read_airplanes("./data/models.csv")
    airports.read_airports("./data/airports.csv")
    tickets.read_tickets("./data/tickets.csv")


def get_search_values(choice):
    values = {
        "origin": None,
        "arrival": None,
        "departure_date": None,
        "arrival_date": None,
        "departure_time": None,
        "arrival_time": None,
        "airline": None,
    }
    if choice == "1":
        values["origin"] = inputs.destination_input("polazište")
    elif choice == "2":
        values["arrival"] = inputs.destination_input("dolazište")
    elif choice == "3":
        values["departure_date"] = inputs.date_input("datum polaska")
    elif choice == "4":
        values["arrival_date"] = inputs.date_input("datum dolaska")
    elif choice == "5":
        values["departure_time"] = inputs.time_input("vreme polaska")
    elif choice == "6":
        values["arrival_time"] = inputs.time_input("vreme dolaska")
    elif choice == "7":
        values["airline"] = inputs.airline_input()
    return values


def read_search_choices(prompt, allow_multiple):
    raw = input(prompt).strip()
    if raw == "8":
        return None
    if allow_multiple:
        choices = [c.strip() for c in raw.split(",") if c.strip()]
    else:
        choices = [raw]
    if "8" in choices:
        return None
    valid = {"1", "2", "3", "4", "5", "6", "7"}
    for c in choices:
        if c not in valid:
            raise Exception("Pogrešan izbor")
    return choices


def flight_single_search():
    scheduled.print_flights(scheduled.merge_flights())
    while True:
        menus.search_flights_menu()
        try:
            choices = read_search_choices("Unesite svoj izbor: ", allow_multiple=False)
            if choices is None:
                print("Pretraga prekinuta!")
                break
            vals = get_search_values(choices[0])
            scheduled.search_flights(**vals)
            break
        except Exception:
            print("Pogrešan izbor!")


def flight_multiple_search():
    while True:
        scheduled.print_flights(scheduled.merge_flights())
        menus.search_flights_menu()
        try:
            choices = read_search_choices("Unesite svoje izbore(1,2,3): ", allow_multiple=True)
            if choices is None:
                print("Pretraga prekinuta!")
                break
            combined = {
                "origin": None,
                "arrival": None,
                "departure_date": None,
                "arrival_date": None,
                "departure_time": None,
                "arrival_time": None,
                "airline": None,
            }
            for choice in choices:
                vals = get_search_values(choice)
                for k, v in vals.items():
                    if v is not None:
                        combined[k] = v
            scheduled.search_flights(**combined)
            break
        except Exception:
            print("Pogrešan izbor!")


def cheapest_flights():
    scheduled.print_flights(scheduled.merge_flights())
    origin = inputs.destination_input("polazište")
    arrival = inputs.destination_input("dolazište")
    scheduled.view_cheapest_flights(origin, arrival)


def flexible_flights():
    scheduled.print_flights(scheduled.merge_flights())
    origin = inputs.destination_input("polazište")
    arrival = inputs.destination_input("dolazište")
    departure_date = inputs.date_input("datum polaska")
    arrival_date = inputs.date_input("datum dolaska")
    flex_days_origin = inputs.flex_days_input("polaska")
    flex_days_arrival = inputs.flex_days_input("dolaska")
    scheduled.flexible_search(origin, arrival, departure_date, flex_days_origin, arrival_date, flex_days_arrival)


def ticket_purchase():
    while True:
        print("***** KUPOVINA KARTE *****")
        scheduled.view_upcoming_flights()
        sched_id = inputs.scheduled_id_input()
        flight = scheduled.select_flight(sched_id)
        if flight:
            while True:
                print("Za koga kupujete kartu?")
                print("1. Za sebe")
                print("2. Za drugu osobu")
                choice = input("Unesite svoj izbor: ").strip()
                if choice not in ["1", "2"]:
                    print("Pogrešan izbor!")
                    continue
                else:
                    user = {}
                    if choice == "1":
                        user = {**users.logged_user}
                    else:
                        name = inputs.name_input("ime")
                        surname = inputs.name_input("prezime")
                        user = users.find_by_name_and_surname(name, surname)
                        if user == None:
                            user = {**users.logged_user, "name": name, "surname": surname}          # kopira user i menja ime i prezime
                    seller = "None"
                    ticket = tickets.make_ticket(flight, user, seller)
                    tickets.write_ticket(ticket, "./data/tickets.csv")
                    print("Uspešno ste kupili kartu!")
                    break
            break
        else:
            break


def customer_tickets():
    upcoming_tickets = tickets.find_user_tickets(users.logged_user["username"])
    tickets.print_tickets(upcoming_tickets)


def customer_check_in():
    user_tickets = tickets.find_user_tickets(users.logged_user["username"])
    available_tickets = tickets.find_soon_tickets(user_tickets)
    tickets.print_tickets(available_tickets)
    if available_tickets:
        ticket_id = inputs.ticket_id_input(available_tickets)
        ticket = tickets.select_ticket(ticket_id)
        tickets.enter_remaining_info(ticket)
        flight = scheduled.select_flight(ticket["flight_id"])
        scheduled.print_rows(flight)
        seat = inputs.seat_input(flight)
        ticket["reserved"] = seat
        scheduled.take_seat(flight, seat)
        tickets.write_all_tickets("./data/tickets.csv")


def sell_ticket():
    while True:
        print("***** PRODAJA KARTE *****")
        scheduled.view_upcoming_flights()
        sched_id = inputs.scheduled_id_input()
        flight = scheduled.select_flight(sched_id)
        if flight:  
            name = inputs.name_input("ime")
            surname = inputs.name_input("prezime")
            user = users.find_by_name_and_surname(name, surname)
            if user == None:
                user = {}
                phone_number = inputs.phone_number_input()
                email = inputs.email_input()
                user["username"] = users.logged_user["username"]
                user["name"] = name
                user["surname"] = surname
                user["phone_number"] = phone_number
                user["email"] = email
                user["passport_number"] = ""
                user["nationality"] = ""
                user["gender"] = ""
            seller = users.logged_user["username"]                  # prodavac
            ticket = tickets.make_ticket(flight, user, seller)
            tickets.write_ticket(ticket, "./data/tickets.csv")
            print("Karta uspešno prodata!")
            break
        else:
            break


def seller_check_in():
    unreserved_tickets = tickets.find_unreserved_tickets()
    available_tickets = tickets.find_soon_tickets(unreserved_tickets)
    tickets.print_tickets(available_tickets)
    if available_tickets:
        ticket_id = inputs.ticket_id_input(available_tickets)
        ticket = tickets.select_ticket(ticket_id)
        tickets.enter_remaining_info(ticket)
        flight = scheduled.select_flight(ticket["flight_id"])
        scheduled.print_rows(flight)
        seat = inputs.seat_input(flight)
        ticket["reserved"] = seat
        scheduled.take_seat(flight, seat)
        tickets.write_all_tickets("./data/tickets.csv")
        print("Let uspešno rezervisan!")


def ticket_update():
    tickets.print_tickets(tickets.tickets)
    if tickets.tickets:
        print("***** IZMENA KARTE *****")
        ticket_id = inputs.ticket_id_input(tickets.tickets)
        sched_id = inputs.existing_scheduled_id_input(scheduled.scheduled_flights)
        flight = scheduled.select_flight(sched_id)
        ticket = tickets.select_ticket(ticket_id)
        departure_date = inputs.date_input("datum polaska")
        scheduled.print_rows(flight)
        seat = inputs.optional_seat_input(flight)
        old_seat = str(ticket.get("reserved")).strip()
        if seat != "None":                       
            if old_seat != "None":
                scheduled.remove_seat(flight, old_seat)     
            scheduled.take_seat(flight, seat)
        ticket["flight_id"] = sched_id
        ticket["origin_airport"] = flight["origin_airport"]
        ticket["arrival_airport"] = flight["arrival_airport"]
        ticket["origin_city"] = flight["origin_city"]
        ticket["arrival_city"] = flight["arrival_city"]
        ticket["departure_date"] = departure_date
        ticket["arrival_date"] = flight["arrival_date"]
        ticket["departure_time"] = flight["departure_time"]
        ticket["arrival_time"] = flight["arrival_time"]
        ticket["airplane_model"] = flight["airplane_model"]
        ticket["price"] = flight["price"]
        ticket["reserved"] = seat
        tickets.write_all_tickets("./data/tickets.csv")
        print("Uspešna izmena!")


def ticket_mark_delete():
    undeleted_tickets = tickets.find_undeleted_tickets()
    tickets.print_tickets(undeleted_tickets)
    if undeleted_tickets:
        print("***** BRISANJE KARTE *****")
        ticket_id = inputs.ticket_id_input(tickets.tickets)
        tickets.mark_ticket(ticket_id)
        print("Karta je uspešno označena za brisanje!")


def sold_ticket_search():
    tickets.print_tickets(tickets.tickets)
    origin = inputs.destination_input("polazište")
    arrival = inputs.destination_input("dolazište")
    departure_date = inputs.date_input("polaska")
    arrival_date = inputs.date_input("dolaska")
    name = inputs.name_input("ime putnika")
    surname = inputs.name_input("prezime putnika")
    searched_tickets = tickets.find_sold_tickets(origin, arrival, departure_date, arrival_date, name, surname, tickets.tickets)
    tickets.print_tickets(searched_tickets)


def flight_create():
    print("***** KREIRANJE LETA *****")
    flight_number = inputs.flight_number_input(flights.flights)
    origin = inputs.destination_input("polazište")
    arrival = inputs.destination_input("dolazište")
    departure_time = inputs.time_input("vreme polaska")
    arrival_time = inputs.time_input("vreme dolaska")
    print("Da li let sleće sledećeg dana?")
    yes_or_no = inputs.yes_or_no_input()
    airline = inputs.airline_input()
    operating_days = inputs.operating_days_input()
    airplane_model = inputs.airplane_model_input()
    price = inputs.price_input()
    flight = {
        "flight_number": flight_number,
        "origin": origin,
        "arrival": arrival,
        "departure_time": departure_time,
        "arrival_time": arrival_time,
        "next_day_arrival": yes_or_no,
        "airline": airline,
        "operating_days": ",".join(operating_days),
        "airplane_model": airplane_model,
        "price": price
    }
    flights.add_flight(flight)
    flights.write_all_flights("./data/flights.csv")
    print("Let uspešno kreiran!")


def flight_update():
    flights.print_flights(flights.flights)
    flight_number = inputs.existing_flight_number_input(flights.flights)
    flight = flights.find_flight(flight_number)
    print("***** IZMENA LETA *****")
    origin = inputs.optional_destination_input("polazište")
    arrival = inputs.optional_destination_input("dolazište")
    departure_time = inputs.optional_time_input("vreme polaska")
    arrival_time = inputs.optional_time_input("vreme dolaska")
    print("Da li let sleće sledećeg dana?")
    next_day_arrival = inputs.optional_yes_or_no_input()
    airline = inputs.optional_airline_input()
    operating_days = inputs.optional_operating_days_input()
    airplane_model = inputs.optional_airplane_model_input()
    price = inputs.optional_price_input()
    flights.update_flight(flight, origin, arrival, departure_time, arrival_time, next_day_arrival, airline, operating_days,airplane_model, price)
    flights.write_all_flights("./data/flights.csv")
    print("Let uspešno izmenjen!")


def ticket_delete():
    marked_tickets = tickets.find_marked_tickets()
    tickets.print_tickets(marked_tickets)
    while True:
        print("***** BRISANJE KARATA *****")
        print("1. Obriši sve karte")
        print("2. Obriši jednu kartu")
        print("3. Obriši više karata")
        print("4. Poništi brisanje za jednu kartu")
        print("5. Poništi brisanje za više karata")
        print("6. Izlaz")
        delete_choice = input("Unesite vaš izbor: ").strip()
        if delete_choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Pogrešan izbor!")
            continue
        if delete_choice == "6":
            break
        selected_tickets = {}
        deleting = False
        if delete_choice == "1":
            selected_tickets = {**marked_tickets}
            deleting = True
        elif delete_choice == "2":
            ticket_id = inputs.ticket_id_input(marked_tickets)
            ticket = tickets.select_ticket(ticket_id)
            selected_tickets[ticket_id] = ticket
            deleting = True
        elif delete_choice == "3":
            while True:
                ticket_id = inputs.ticket_id_input(marked_tickets)
                if ticket_id in selected_tickets:
                    print("Već ste uneli tu kartu! Unesite neku drugu!")
                    continue
                ticket = tickets.select_ticket(ticket_id)
                selected_tickets[ticket_id] = ticket
                if len(selected_tickets) != len(marked_tickets):
                    print("Želite li da obrišete još karata?")
                    yes_or_no = inputs.yes_or_no_input()
                    if yes_or_no == "da":
                        continue
                break
            deleting = True
        elif delete_choice == "4":
            ticket_id = inputs.ticket_id_input(marked_tickets)
            ticket = tickets.select_ticket(ticket_id)
            selected_tickets[ticket_id] = ticket
            deleting = False
        elif delete_choice == "5":
            while True:
                ticket_id = inputs.ticket_id_input(marked_tickets)
                if ticket_id in selected_tickets:
                    print("Već ste uneli tu kartu! Unesite neku drugu!")
                    continue
                ticket = tickets.select_ticket(ticket_id)
                selected_tickets[ticket_id] = ticket
                if len(selected_tickets) != len(marked_tickets):
                    print("Želite li da poništite brisanje za još karata?")
                    yes_or_no = inputs.yes_or_no_input()
                    if yes_or_no == "da":
                        continue
                break
            deleting = False
        print("Da li ste sigurni?") 
        yes_or_no = inputs.yes_or_no_input()
        if yes_or_no == "da" and deleting == True:
            tickets.delete_tickets(selected_tickets)
            print("Karta/e uspešno izbrisane!")
            break
        elif yes_or_no == "da" and deleting == False:
            tickets.remove_delete_marks(selected_tickets)
            print("Karte uspešno vraćene!")
            break
        elif yes_or_no == "ne":
            print("Otkazano!")
            break


def manager_reports():
    while True:
        print("\n\n***** SVE KARTE *****" )
        tickets.print_tickets(tickets.tickets)
        menus.reports_menu()
        choice = input("Unesite svoj izbor: ").strip().lower()
        if choice == "a":
            date = inputs.date_input("datum prodaje")
            results = tickets.find_by_sold_date(date, tickets.tickets)
            tickets.print_tickets(results)
            break
        elif choice == "b":
            date = inputs.date_input("datum polaska")
            results = tickets.find_by_departure_date(date, tickets.tickets)
            tickets.print_tickets(results)
            break
        elif choice == "c":
            date = inputs.date_input("datum prodaje")
            sold_tickets = tickets.find_by_sold_date(date, tickets.tickets)
            seller = inputs.username_login_input()
            results = tickets.find_by_seller(seller, sold_tickets)
            tickets.print_tickets(results)
            break
        elif choice == "d":
            date = inputs.date_input("datum prodaje")
            results = tickets.find_by_sold_date(date, tickets.tickets)
            tickets.print_tickets(results)
            if results:
                print("Ukupan broj karata: ", tickets.count_tickets(results))
                print("Ukupna cena karata: ", tickets.total_price(results))
            break
        elif choice == "e":
            date = inputs.date_input("datum polaska")
            results = tickets.find_by_departure_date(date, tickets.tickets)
            tickets.print_tickets(results)
            if results:
                print("Ukupan broj karata: ", tickets.count_tickets(results))
                print("Ukupna cena karata: ", tickets.total_price(results))
            break
        elif choice == "f":
            date = inputs.date_input("datum prodaje")
            sold_tickets = tickets.find_by_sold_date(date, tickets.tickets)
            seller = inputs.username_login_input()
            results = tickets.find_by_seller(seller, sold_tickets)
            tickets.print_tickets(results)
            if results:
                print("Ukupan broj karata: ", tickets.count_tickets(results))
                print("Ukupna cena karata: ", tickets.total_price(results))
            break
        elif choice == "g":
            results = tickets.last_30_days_by_seller()
            tickets.print_sales_by_sellers(results)
            break
        elif choice == "x":
            break
        else:
            print("Pogrešan izbor!")