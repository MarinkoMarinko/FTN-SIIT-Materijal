import uuid
import tabulate
import datetime


from utils import inputs
from services import scheduled


tickets = {}


def read_tickets(filename):
    global tickets
    tickets = {}
    with open(filename, encoding="UTF-8") as file:
        for line in file:
            data = line.strip().split("|")
            ticket = {
                "ticket_id": data[0],
                "flight_id": data[1],
                "origin_airport": data[2],
                "origin_city": data[3],
                "arrival_airport": data[4],
                "arrival_city": data[5],
                "departure_date": data[6],
                "departure_time": data[7],
                "arrival_date": data[8],
                "arrival_time": data[9],
                "airplane_model": data[10],
                "price": float(data[11]),
                "reserved": data[12],
                "username": data[13],
                "name": data[14],
                "surname": data[15],
                "phone_number": data[16],
                "email": data[17],
                "passport_number": data[18],
                "nationality": data[19],
                "gender": data[20],
                "sold_by": data[21],
                "sold_on": data[22],
                "delete": data[23]
            }
            tickets[ticket["ticket_id"]] = ticket


def make_ticket(flight, user, seller):
    global tickets
    ticket_id = uuid.uuid4().hex[:10].upper()        
    ticket = {
        "ticket_id": ticket_id,
        "flight_id": flight.get("id"),
        "origin_airport": flight.get("origin_airport"),
        "origin_city": flight.get("origin_city"),
        "arrival_airport": flight.get("arrival_airport"),
        "arrival_city": flight.get("arrival_city"),
        "departure_date": flight.get("departure_date"),
        "departure_time": flight.get("departure_time"),
        "arrival_date": flight.get("arrival_date"),
        "arrival_time": flight.get("arrival_time"),
        "airplane_model": flight.get("airplane_model"),
        "price": flight.get("price"),
        "reserved": "None",                       # rezervisano sediste
        "username": user["username"],
        "name": user["name"],
        "surname": user["surname"],
        "phone_number": user["phone_number"],
        "email": user["email"],
        "passport_number": user["passport_number"],
        "nationality": user["nationality"],
        "gender": user["gender"],
        "sold_by": seller,
        "sold_on": datetime.datetime.now().strftime("%d.%m.%Y"),                # danasnji datum
        "delete": ""                               # flag za brisanje
    }  
    tickets[ticket["ticket_id"]] = ticket
    return ticket
    

def write_ticket(ticket, filename):
    with open(filename, "a", encoding="UTF-8") as file:
        file.write("|".join(map(str, ticket.values())) + "\n")


def write_all_tickets(filename):
    open(filename, "w", encoding="UTF-8").close()   
    for ticket in tickets.values():                
        write_ticket(ticket, filename)


def print_tickets(tickets):
    if not tickets:
        print("Nema karata za prikaz.")
        return
    rows = []
    for ticket in tickets.values():
        rows.append([
            ticket["ticket_id"],
            ticket["flight_id"],   
            f'{ticket["origin_airport"]} → '
            f'{ticket["arrival_airport"]}',
            f'{ticket["departure_date"]} {ticket["departure_time"]}',
            f'{ticket["arrival_date"]} {ticket["arrival_time"]}',
        ])
    headers = [
        "Broj karte",
        "ID leta",
        "Relacija",
        "Vreme polaska",
        "Vreme dolaska",
    ]
    print(tabulate.tabulate(rows, headers=headers, tablefmt="grid"))


def find_unreserved_tickets():
    unreserved_tickets = {}
    for ticket_id, ticket in tickets.items():
        if ticket.get("reserved") == "None":
            unreserved_tickets[ticket_id] = ticket
    return unreserved_tickets


def find_reserved_tickets():
    reserved_tickets = {}
    for ticket_id, ticket in tickets.items():
        if ticket.get("reserved") != "None":
            reserved_tickets[ticket_id] = ticket
    return reserved_tickets


def find_user_tickets(username):
    user_tickets = {}
    for ticket_id, ticket in tickets.items():
        if ticket.get("username") == username and ticket.get("reserved") == "None":
            user_tickets[ticket_id] = ticket
    return user_tickets


def find_soon_tickets(tickets):
    soon_tickets = {}
    today = datetime.datetime.today().date()
    limit_date = today + datetime.timedelta(days=2)
    for ticket_id, ticket in tickets.items():
        dep_date = datetime.datetime.strptime(
            ticket["departure_date"], "%d.%m.%Y"
        ).date()
        if today <= dep_date <= limit_date:
            soon_tickets[ticket_id] = ticket
    return soon_tickets


def find_sold_tickets(origin, arrival, departure_date, arrival_date, name, surname, tickets):
    merged_flights = scheduled.merge_flights()
    results = {}
    for ticket_id, ticket in tickets.items():
        flight = merged_flights.get(ticket["flight_id"])
        if not flight:
            continue
        if flight.get("origin") != origin:
            continue
        if flight.get("arrival") != arrival:
            continue
        if ticket.get("departure_date") != departure_date:
            continue
        if ticket.get("arrival_date") != arrival_date:
            continue
        if ticket.get("name") != name:
            continue
        if ticket.get("surname") != surname:
            continue
        results[ticket_id] = ticket
    return results


def select_ticket(ticket_id):
    if ticket_id in tickets:
        return tickets[ticket_id]
    return None 


def enter_remaining_info(ticket):
    if ticket["passport_number"] == "":
        ticket["passport_number"] = inputs.passport_number_ticket_input()
    if ticket["nationality"] == "":
        ticket["nationality"] = inputs.nationality_ticket_input()
    if ticket["gender"] == "":
        ticket["gender"] = inputs.gender_ticket_input()


def find_undeleted_tickets():
    undeleted_tickets = {}
    for ticket_id, ticket in tickets.items():
        if ticket["delete"] != "DELETE":
            undeleted_tickets[ticket_id] = ticket
    return undeleted_tickets


def find_marked_tickets():
    deleted_tickets = {}
    for ticket_id, ticket in tickets.items():
        if ticket["delete"] == "DELETE":
            deleted_tickets[ticket_id] = ticket
    return deleted_tickets


def mark_ticket(ticket_id):
    ticket = select_ticket(ticket_id)
    ticket["delete"] = "DELETE"
    write_all_tickets("./data/tickets.csv")


def delete_tickets(deleted_tickets):
    global tickets
    for ticket_id in deleted_tickets:
        tickets.pop(ticket_id)
    write_all_tickets("./data/tickets.csv")


def remove_delete_marks(marked_tickets):
    global tickets
    for ticket_id in marked_tickets:
        tickets[ticket_id]["delete"] = ""
    write_all_tickets("./data/tickets.csv")


def find_by_sold_date(date, selected_tickets):
    global tickets
    results = {}
    for ticket_id, ticket in selected_tickets.items():
        if ticket["sold_on"] == date:
            results[ticket_id] = ticket
    return results


def find_by_departure_date(date, selected_tickets):
    results = {}
    for ticket_id, ticket in selected_tickets.items():
        if ticket["departure_date"] == date:
            results[ticket_id] = ticket
    return results


def find_by_seller(seller, sold_tickets):
    results = {}
    for ticket_id, ticket in sold_tickets.items():
        if ticket["sold_by"] == seller:
            results[ticket_id] = ticket
    return results


def count_tickets(sold_tickets):
    count = 0
    for ticket in sold_tickets.values():
        count += 1
    return count


def total_price(sold_tickets):
    price = 0
    for ticket in sold_tickets.values():
        price += ticket["price"]
    return price


def last_30_days_by_seller():
    today = datetime.datetime.now().date()
    cutoff = today - datetime.timedelta(days=30)
    results = {}
    for ticket in tickets.values():
        sold_by = ticket.get("sold_by")
        sold_on = ticket.get("sold_on")
        sold_date = datetime.datetime.strptime(sold_on, "%d.%m.%Y").date()
        if not (cutoff <= sold_date <= today):
            continue
        if sold_by == "None":
            continue
        if sold_by not in results:
            results[sold_by] = {"count": 0, "total": 0.0}
        results[sold_by]["count"] += 1
        results[sold_by]["total"] += float(ticket.get("price"))
    return results


def print_sales_by_sellers(results):
    if not results:
        print("Nema prodatih karata u poslednjih 30 dana.")
        return
    rows = []
    for seller, data in results.items():
        rows.append([
            seller,
            data["count"],
            f"{data['total']:.2f}"
        ])
    headers = ["Prodavac", "Broj prodatih karata", "Ukupna cena"]
    print(tabulate.tabulate(rows, headers=headers, tablefmt="grid"))