airplanes = {}


def read_airplanes(filename):
    with open(filename, encoding="UTF-8") as file:
        for line in file:
            airplane_data = line.strip().split("|")
            airplane = {
                "model": airplane_data[0],
                "row_count": int(airplane_data[1]),
                "rows": [row.split(",") for row in airplane_data[2].split(";")]     # [A,B,C,D], [A,B,C,D]... 
            }
            airplanes[airplane["model"]] = airplane