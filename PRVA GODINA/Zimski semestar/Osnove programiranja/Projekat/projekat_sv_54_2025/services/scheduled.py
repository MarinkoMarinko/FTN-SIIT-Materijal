import tabulate
import datetime


from services import flights
from services import airplanes
from services import airports
from services import tickets


scheduled_flights = {}


def read_scheduled(filename):
    global scheduled_flights
    with open(filename, encoding="UTF-8") as file:
        for line in file:
            scheduled_data = line.strip().split("|")
            flight = {
                "id": scheduled_data[0],
                "flight_number": scheduled_data[1],
                "departure_date": scheduled_data[2],
                "arrival_date": scheduled_data[3]
            }
            scheduled_flights[flight["id"]] = flight


def merge_flights():
    global scheduled_flights
    merged = {}
    for sched in scheduled_flights.values():
        fn = sched["flight_number"]
        if fn not in flights.flights:
            continue
        flight = flights.flights[fn]
        model = flight.get("airplane_model")
        plane = airplanes.airplanes.get(model)
        origin_code = flight.get("origin")
        arrival_code = flight.get("arrival")
        origin_airport = airports.airports.get(origin_code)
        arrival_airport = airports.airports.get(arrival_code)
        rows = [r.copy() for r in plane["rows"]] if plane else None
        merged_flight = {
            "id": sched["id"],
            **flight,
            "departure_date": sched["departure_date"],
            "arrival_date": sched["arrival_date"],
            "row_count": plane["row_count"] if plane else None,
            "rows": rows,
            "origin_airport": origin_airport["airport"] if origin_airport else None,
            "origin_city": origin_airport["city"] if origin_airport else None,
            "origin_country": origin_airport["country"] if origin_airport else None,
            "arrival_airport": arrival_airport["airport"] if arrival_airport else None,
            "arrival_city": arrival_airport["city"] if arrival_airport else None,
            "arrival_country": arrival_airport["country"] if arrival_airport else None,
        }
        for t in tickets.tickets.values():
            if t.get("flight_id") == sched["id"] and t.get("reserved") != "None":
                take_seat(merged_flight, t["reserved"])
        merged[sched["id"]] = merged_flight
    return merged


def print_flights(flights):
    if not flights:
        print("Nema takvih podataka za prikaz!")
        return
    rows = []
    for sched_id, flight in flights.items():
        rows.append([
            sched_id,
            flight.get("flight_number"),
            f'{flight.get("origin")} ({flight.get("origin_city")})',
            f'{flight.get("arrival")} ({flight.get("arrival_city")})',
            f'{flight.get("departure_date")} {flight.get("departure_time")}',
            f'{flight.get("arrival_date")} {flight.get("arrival_time")}',
            flight.get("airline"),
            f'{float(flight.get("price", 0)):.2f}'
        ])
    headers = [
        "ID",
        "Let",
        "Polazak",
        "Dolazak",
        "Poletanje",
        "Sletanje",
        "Prevoznik",
        "Cena (€)"
    ]
    print(tabulate.tabulate(rows, headers=headers, tablefmt="grid", stralign="left"))


def view_upcoming_flights():
    merged_flights = merge_flights()
    upcoming_flights = {}
    today = datetime.date.today()
    for sched_id, flight in merged_flights.items():
        dep_date = datetime.datetime.strptime(flight["departure_date"],"%d.%m.%Y").date()
        if dep_date > today:
            upcoming_flights[sched_id] = flight
    print_flights(upcoming_flights)


def view_cheapest_flights(origin, arrival):
    merged_flights = merge_flights()
    cheapest_flights = {}
    for sched_id, flight in merged_flights.items():
        if flight["origin"] == origin and flight["arrival"] == arrival:
            cheapest_flights[sched_id] = flight
    if not cheapest_flights:
        print("Nema podataka za datu relaciju!")
        return
    sorted_by_price = sorted(cheapest_flights.items(), key=lambda x: x[1]["price"])
    cheapest_10 = sorted_by_price[:10]              # 10 najjeftinijih
    cheapest_10.sort(key=lambda x: x[1]["price"], reverse=True)     # sortiranje po opadajucoj
    print_flights(dict(cheapest_10))


def search_flights(origin, arrival, departure_date, arrival_date, departure_time, arrival_time, airline):
    merged = merge_flights()
    search_results = {}
    for sched_id, flight in merged.items():
        if origin and flight["origin"] != origin:
            continue
        if arrival and flight["arrival"] != arrival:
            continue
        if departure_date and flight["departure_date"] != departure_date:
            continue
        if arrival_date and flight["arrival_date"] != arrival_date:
            continue
        if departure_time and flight["departure_time"] != departure_time:
            continue
        if arrival_time and flight["arrival_time"] != arrival_time:
            continue
        if airline and flight["airline"] != airline:
            continue
        search_results[sched_id] = flight
    print_flights(search_results)


def parse_date(s):
    return datetime.datetime.strptime(s, "%d.%m.%Y").date()


def in_range(d, start, end):
    return start <= d <= end


def flexible_search(origin, arrival, dep_date_str, dep_flex_days, arr_date_str, arr_flex_days):
    merged = merge_flights()
    dep_center = parse_date(dep_date_str)
    dep_start = dep_center - datetime.timedelta(days=dep_flex_days)
    dep_end   = dep_center + datetime.timedelta(days=dep_flex_days)
    arr_center = parse_date(arr_date_str)
    arr_start = arr_center - datetime.timedelta(days=arr_flex_days)
    arr_end   = arr_center + datetime.timedelta(days=arr_flex_days)
    results = {}
    for sched_id, flight in merged.items():
        if flight.get("origin") != origin:
            continue
        if flight.get("arrival") != arrival:
            continue
        dep_date = parse_date(flight["departure_date"])
        arr_date = parse_date(flight["arrival_date"])
        if not in_range(dep_date, dep_start, dep_end):
            continue
        if not in_range(arr_date, arr_start, arr_end):
            continue
        results[sched_id] = flight
    sorted_items = sorted(results.items(), key=lambda x: x[1]["price"], reverse=True)
    print_flights(dict(sorted_items))


def has_space(flight):
    rows = flight.get("rows")
    if rows == None:
        return False
    return any(
        seat != "X"
        for row in flight["rows"]
        for seat in row
    )


def select_flight(flight_id):
    flights = merge_flights()
    if flight_id not in flights:
        print("Ne postoji let sa unetim brojem!")
        return
    elif has_space(flights[flight_id]) == False:
        print("Let nema slobodnih mesta!")
        return
    else:
        return flights[flight_id]
    

def print_rows(flight):
    for i in range(1, flight["row_count"] + 1):
        print(f"Red {i}: {' '.join(flight['rows'][i-1])}")


def take_seat(flight, seat):
    row = int(seat[0])
    letter = seat[1]
    row_index = row - 1
    row_seats = flight["rows"][row_index]
    for i, s in enumerate(row_seats):
        if s == letter:
            row_seats[i] = "X"
            return
        

def remove_seat(flight, seat):
    row = int(seat[0])
    letter = seat[1]
    row_index = row - 1
    col_index = ord(letter) - ord('A')              # vraca indeks da bih znao koje slovo da vratim umesto X
    flight["rows"][row_index][col_index] = letter