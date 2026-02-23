from utils import inputs


users = {}
logged_user = None


def read_users(filename):
    global users
    with open(filename, encoding="UTF-8") as file:
        for line in file:
            data = line.strip().split("|")
            user = {
                "username": data[0],
                "password": data[1],
                "name": data[2],
                "surname": data[3],
                "role": data[4],
                "passport_number": data[5],
                "nationality": data[6],
                "phone_number": data[7],
                "email": data[8],
                "gender": data[9]
            }
            users[user["username"]] = user


def write_user(filename, user):
    with open(filename, "a", encoding="UTF-8") as file:
        file.write("|".join(data for data in user.values()))
        file.write("\n")


def is_logged_in():
    return logged_user is not None


def has_role(role):
    if logged_user is None:
        return False
    return logged_user.get("role") == role


def login():
    global logged_user
    global users
    username = inputs.username_login_input()
    password = inputs.password_login_input(username)
    logged_user = users[username]
    print("Uspešno ste se prijavili!")


def logout():
    global logged_user
    logged_user = None
    print("Uspešno ste se odjavili!")


def register(role):
    global users
    username = inputs.username_register_input()
    password = inputs.password_register_input()
    name = inputs.name_input("ime")
    surname = inputs.name_input("prezime")
    role = role
    passport_number = inputs.passport_number_input()
    nationality = inputs.nationality_input()
    phone_number = inputs.phone_number_input()
    email = inputs.email_input()
    gender = inputs.gender_input()
    user = {
        "username": username,
        "password": password,
        "name": name,
        "surname": surname,
        "role": role,
        "passport_number": passport_number,
        "nationality": nationality,
        "phone_number": phone_number,
        "email": email,
        "gender": gender
    } 
    users[user["username"]] = user
    write_user("./data/users.csv", user)

    
def find_by_name_and_surname(name, surname):
    global users
    for user in users.values():
        if user["name"] == name and user["surname"] == surname:
            return user