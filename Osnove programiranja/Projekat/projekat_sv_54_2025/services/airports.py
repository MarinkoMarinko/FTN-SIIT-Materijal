airports = {}


def read_airports(filename):
    with open(filename, encoding="UTF-8") as file:
        for line in file:
            airport_data = line.strip().split("|")
            airport = {
                "IATA": airport_data[0],
                "airport": airport_data[1],
                "city": airport_data[2],
                "country": airport_data[3]
            }
            airports[airport["IATA"]] = airport