import re
import datetime


from services import users


def user_exists(username):
    return username in users.users


def username_login_input():
    while True:
        username = input("Unesite korisničko ime: ").strip()
        if len(username) < 5:
            print("Korisničko ime mora sadržati bar 5 karaktera!")
        elif user_exists(username) == False:
            print(f"Ne postoji korisnik sa korisničkim imenom {username}")
        else:
            return username
        

def username_register_input():
    while True:
        username = input("Unesite korisničko ime: ").strip()
        if len(username) < 5:
            print("Korisničko ime mora sadržati bar 5 karaktera!")
        elif user_exists(username) == True:
            print(f"Korisnik sa korisničkim imenom {username} već postoji!")
        else:
            return username
        

def correct_password(username, password):
    return users.users[username]["password"] == password


def password_login_input(username):
    while True:
        password = input("Unesite lozinku: ").strip()
        if len(password) < 7:
            print("Lozinka mora sadržati bar 7 karaktera!")
        elif correct_password(username, password) == False:
            print("Pogrešna lozinka!")
        else:
            return password
        

def password_register_input():
    while True:
        password = input("Unesite lozinku: ").strip()
        if len(password) < 7:
            print("Lozinka mora sadržati bar 7 karaktera!")
        else:
            return password
        

def phone_number_input():
    while True:
        phone_number = input("Unesite broj telefona: ").strip()
        if len(phone_number) not in [9, 10]:
            print("Broj telefona mora sadržati 9 ili 10 cifara!")
        elif phone_number.isnumeric() == False:
            print("Broj telefona može sadržati samo cifre!")
        else:
            return phone_number
        

def valid_email(email):
    EMAIL_REGEX = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(EMAIL_REGEX, email) is not None
def email_input():
    while True:
        email = input("Unesite email: ").strip()
        if valid_email(email) == False:
            print("Uneli ste nevalidan email!")
        else:
            return email
        

def name_input(name_type):
    while True:
        name = input(f"Unesite {name_type}: ").strip().capitalize()
        if len(name) < 3:
            print(f"{name_type.capitalize()} mora sadržati bar 3 slova!")
        elif name.isalpha() == False:
            print(f"{name_type.capitalize()} mora sadržati samo slova!")
        else:
            return name
        

def passport_number_input():
    while True:
        passport_number = input("Unesite broj pasoša (Enter da preskočite): ").strip()
        if len(passport_number) != 0 and len(passport_number) != 9:
            print("Broj pasoša mora sadržati tačno 9 cifara!")
        elif len(passport_number) != 0 and passport_number.isnumeric() == False:
            print("Broj pasoša mora sadržati samo cifre!")
        else:
            return passport_number
        

def nationality_input():
    while True:
        nationality = input("Unesite nacionalnost: (Enter da preskočite): ").strip()
        if len(nationality) != 0 and nationality.isalpha() == False:
            print("Nacionalnost mora sadržati samo slova!")
        else:
            return nationality
        

def gender_input():
    while True:
        gender = input("Unesite pol: M ili Z (Enter da preskočite): ").strip().upper()
        if len(gender) != 0 and len(gender) != 1:
            print("Pol može sadržati samo 1 slovo!")
        elif len(gender) != 0 and gender not in ["M", "Z"]:
            print("Morate uneti M ili Z!")
        else:
            return gender
        

def destination_input(destination_type):
    while True:
        destination = input(f"Unesite {destination_type}: ").strip().upper()
        if len(destination) != 3:
            print(f"{destination_type.capitalize()} mora sadržati tačno 3 slova!")
        elif destination.isalpha() == False:
            print(f"{destination_type.capitalize()} mora sadržati samo slova!")
        else:
            return destination
        

def valid_date(date_str):
    try:
        day, month, year = map(int, date_str.split("."))
        input_date = datetime.date(year, month, day)
        return True
    except ValueError:
        return False
    

def date_input(date_type):
    while True:
        date = input(f"Unesite {date_type} (dd.mm.yyyy): ").strip()
        if valid_date(date) == False:
            print(f"Uneli ste {date_type} u pogrešnom formatu!")
        else:    
            return date
        

def valid_time(time_str):
    try:
        hour, minute = map(int, time_str.split(":"))
        return (
            len(time_str) == 5 and
            0 <= hour <= 23 and
            0 <= minute <= 59
        )
    except ValueError:
        return False
    

def time_input(time_type):
    while True:
        time = input(f"Unesite {time_type} (hh:mm): ").strip()
        if valid_time(time) == False:
            print(f"Uneli ste {time_type} u pogrešnom formatu!")
        else:
            return time
        

def airline_input():
    while True:
        airline = input("Unesite naziv prevoznika: ").strip()
        if len(airline) < 5:
            print("Naziv prevoznika mora sadržati bar 5 karaktera!")
        else:
            return airline
        

def flex_days_input(flex_days_type):
    while True:
        try:
            flex_days = eval(input(f"Unesite broj fleksibilnih dana {flex_days_type}: ").strip())
            if flex_days <= 0:
                print("Morate uneti broj veći od 0!")
            else:
                return flex_days
        except Exception:
            print("Morate uneti broj!")


def scheduled_id_input():
    while True:
        sched_id = input("Unesite broj konkretnog leta: ").strip()
        if len(sched_id) != 4:
            print("Broj konkretnog leta mora sadržati tačno 4 cifre!")
        elif sched_id.isnumeric() == False:
            print("Broj konkretnog leta mora sadržati samo cifre!")
        else:
            return sched_id
        

def existing_scheduled_id_input(flights):
    while True:
        sched_id = input("Unesite broj konkretnog leta: ").strip()
        if len(sched_id) != 4:
            print("Broj konkretnog leta mora sadržati tačno 4 cifre!")
        elif sched_id.isnumeric() == False:
            print("Broj konkretnog leta mora sadržati samo cifre!")
        elif sched_id not in flights:
            print("Ne postoji konkretni let sa unetim brojem!")
        else:
            return sched_id
        

def ticket_id_input(available_tickets):
    while True:
        ticket_id = input("Unesite broj karte: ").strip()
        if len(ticket_id) != 10:
            print("Broj karte mora sadržati tačno 10 karaktera")
        elif ticket_id not in available_tickets:
            print("Ne postoji karta sa unetim brojem!")
        else:
            return ticket_id
        

def passport_number_ticket_input():
    while True:
        passport_number = input("Unesite broj pasoša: ").strip()
        if len(passport_number) != 9:
            print("Broj pasoša mora sadržati tačno 9 cifara!")
        elif passport_number.isnumeric() == False:
            print("Broj pasoša mora sadržati samo cifre!")
        else:
            return passport_number
        

def nationality_ticket_input():
    while True:
        nationality = input("Unesite nacionalnost: ").strip()
        if nationality.isalpha() == False:
            print("Nacionalnost mora sadržati samo slova!")
        else:
            return nationality
        

def gender_ticket_input():
    while True:
        gender = input("Unesite pol: M ili Z: ").strip().upper()
        if len(gender) != 1:
            print("Pol može sadržati samo 1 slovo!")
        elif gender not in ["M", "Z"]:
            print("Morate uneti M ili Z!")
        else:
            return gender
        

def seat_input(flight):
    pattern = re.compile(r'^([1-9])([A-Z])$')
    while True:
        seat = input("Unesite broj sedišta (npr. 1A): ").strip().upper()
        match = pattern.match(seat)
        if not match:
            print("Neispravan format! Primer: 1A, 2C")
            continue
        row = int(seat[0])
        letter = seat[1]
        if row < 1 or row > flight["row_count"]:
            print(f"Red mora biti između 1 i {flight['row_count']}.")
            continue
        row_seats = flight["rows"][row - 1]
        if letter not in row_seats:
            print(f"Sedište je već zauzeto!")
            continue
        return seat
    

def optional_seat_input(flight):
    pattern = re.compile(r'^([1-9])([A-Z])$')
    while True:
        seat = input("Unesite broj sedišta (npr. 1A): ").strip().upper()
        if seat == "":
            return "None"
        match = pattern.match(seat)
        if not match:
            print("Neispravan format! Primer: 1A, 2C")
            continue
        row = int(seat[0])
        letter = seat[1]
        if row < 1 or row > flight["row_count"]:
            print(f"Red mora biti između 1 i {flight['row_count']}.")
            continue
        row_seats = flight["rows"][row - 1]
        if letter not in row_seats:
            print(f"Sedište je već zauzeto!")
            continue
        return seat
    

def yes_or_no_input():
    while True:
        yes_or_no = input("Unesite da ili ne: ").strip().lower()
        if yes_or_no not in ["da", "ne"]:
            print("Morate uneti samo da ili ne.")
        else:
            return yes_or_no
        

def flight_number_input(flights):
    while True:
        flight_id = input("Unesite broj leta: ").strip().upper()
        if len(flight_id) != 4:
            print("Broj leta mora sadržati tačno 4 karaktera!")
        elif flight_id[:2].isalpha() == False:
            print("Prva dva karaktera broja leta moraju biti slova!")
        elif flight_id[2:].isnumeric() == False:
            print("Poslednja dva karaktera broja leta moraju biti brojevi!")
        elif flight_id in flights:
            print(f"Broj leta {flight_id} već postoji!")
        else:
            return flight_id
        

def existing_flight_number_input(flights):
    while True:
        flight_id = input("Unesite broj leta: ").strip().upper()
        if len(flight_id) != 4:
            print("Broj leta mora sadržati tačno 4 karaktera!")
        elif flight_id[:2].isalpha() == False:
            print("Prva dva karaktera broja leta moraju biti slova!")
        elif flight_id[2:].isnumeric() == False:
            print("Poslednja dva karaktera broja leta moraju biti brojevi!")
        elif flight_id not in flights:
            print(f"Broj leta {flight_id} ne postoji!")
        else:
            return flight_id
        

def operating_days_input():
    while True:
        try:
            operating_days = input("Unesite sve dane kada se let realizuje (npr. ponedeljak,utorak,sreda): ").strip().lower()
            days = operating_days.split(",")
            for day in days:
                if day not in ["ponedeljak", "utorak", "sreda", "četvrtak", "cetvrtak", "petak", "subota", "nedelja"]:
                    raise Exception
            return days
        except Exception:
            print("Uneli ste dane u pogrešnom formatu!")


def airplane_model_input():
    while True:
        model = input("Unesite model aviona: ").strip()
        if len(model) < 5:
            print("Morate uneti bar 5 karaktera!")
        else:
            return model
        

def price_input():
    while True:
        try:
            price = float(input("Unesite cenu leta: ").strip())
            if price <= 0:
                print("Cena mora biti veća od 0!")
            else:
                return price
        except Exception:
            print("Neispravan unos cene!")


def optional_destination_input(destination_type):
    while True:
        destination = input(f"Unesite {destination_type} (Enter da preskočite): ").strip().upper()
        if len(destination) != 3 and len(destination) != 0:
            print(f"{destination_type.capitalize()} mora sadržati tačno 3 slova!")
        elif destination.isalpha() == False and len(destination) != 0:
            print(f"{destination_type.capitalize()} mora sadržati samo slova!")
        else:
            return destination
        

def optional_time_input(time_type):
    while True:
        time = input(f"Unesite {time_type} (hh:mm) (Enter da preskočite): ").strip()
        if valid_time(time) == False and len(time) != 0:
            print(f"Uneli ste {time_type} u pogrešnom formatu!")
        else:
            return time
        

def optional_yes_or_no_input():
    while True:
        yes_or_no = input("Unesite da ili ne (Enter da preskočite): ").strip().lower()
        if yes_or_no not in ["da", "ne"] and len(yes_or_no) != 0:
            print("Morate uneti samo da ili ne.")
        else:
            return yes_or_no
        

def optional_airline_input():
    while True:
        airline = input("Unesite naziv prevoznika (Enter da preskočite): ").strip()
        if len(airline) < 5 and len(airline) != 0:
            print("Naziv prevoznika mora sadržati bar 5 karaktera!")
        else:
            return airline
        

def optional_operating_days_input():
    while True:
        try:
            operating_days = input("Unesite sve dane kada se let realizuje (npr. ponedeljak,utorak,sreda) (Enter da preskočite): ").strip().lower()
            if operating_days == "":
                return operating_days
            days = operating_days.split(",")
            for day in days:
                if day not in ["ponedeljak", "utorak", "sreda", "četvrtak", "cetvrtak", "petak", "subota", "nedelja"]:
                    raise Exception
            return days
        except Exception:
            print("Uneli ste dane u pogrešnom formatu!")


def optional_airplane_model_input():
    while True:
        model = input("Unesite model aviona (Enter da preskočite): ").strip()
        if len(model) < 5 and len(model) != 0:
            print("Morate uneti bar 5 karaktera!")
        else:
            return model
        
        
def optional_price_input():
    while True:
        try:
            price = input("Unesite cenu leta (Enter da preskočite): ").strip()
            if price == "":
                return price
            price = float(price)
            if price <= 0:
                print("Cena mora biti veća od 0!")
            else:
                return price
        except Exception:
            print("Neispravan unos cene!")