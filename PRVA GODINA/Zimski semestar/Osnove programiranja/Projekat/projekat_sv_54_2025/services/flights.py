import tabulate


flights = {}


def read_flights(filename):
    global flights
    flights = {}
    with open(filename, encoding="UTF-8") as file:
        for line in file:
            flight_data = line.strip().split("|")
            flight = {
                "flight_number": flight_data[0],
                "origin": flight_data[1],
                "arrival": flight_data[2],
                "departure_time": flight_data[3],
                "arrival_time": flight_data[4],
                "next_day_arrival": flight_data[5],
                "airline": flight_data[6],
                "operating_days": flight_data[7],
                "airplane_model": flight_data[8],
                "price": float(flight_data[9])
            }
            flights[flight["flight_number"]] = flight


def write_flight(flight, filename):
    with open(filename, "a", encoding="UTF-8") as file:
        file.write("|".join(map(str, flight.values())) + "\n")


def add_flight(flight):
    global flights
    flights[flight["flight_number"]] = flight


def write_all_flights(filename):
    global flights
    with open(filename, "w", encoding="UTF-8") as file:
        for flight in flights.values():
            write_flight(flight, filename)


def print_flights(flights):
    headers = [
        "Broj leta",
        "Polazište",
        "Odredište",
        "Vreme polaska",
        "Vreme dolaska",
        "Prevoznik",
        "Cena (€)"
    ]
    rows = []
    for flight in flights.values():
        rows.append([
            flight["flight_number"],
            flight["origin"],
            flight["arrival"],
            flight["departure_time"],
            flight["arrival_time"] + (" (+1)" if flight["next_day_arrival"] == "da" else ""),
            flight["airline"],
            flight["price"]
        ])
    print(tabulate.tabulate(rows, headers=headers, tablefmt="grid"))


def find_flight(flight_number):
    global flights
    return flights[flight_number]


def update_flight(flight, origin, arrival, departure_time, arrival_time, next_day_arrival, airline, operating_days,airplane_model, price):
    flight["origin"] = origin if origin != "" else flight["origin"]
    flight["arrival"] = arrival if arrival != "" else flight["arrival"]
    flight["departure_time"] = departure_time if departure_time != "" else flight["departure_time"]
    flight["arrival_time"] = arrival_time if arrival_time != "" else flight["arrival_time"]
    flight["next_day_arrival"] = next_day_arrival if next_day_arrival != "" else flight["next_day_arrival"]
    flight["airline"] = airline if airline != "" else flight["airline"]
    flight["operating_days"] = ",".join(operating_days) if operating_days != "" else flight["operating_days"]
    flight["airplane_model"] = airplane_model if airplane_model != "" else flight["airplane_model"]
    flight["price"] = price if price != "" else flight["price"]