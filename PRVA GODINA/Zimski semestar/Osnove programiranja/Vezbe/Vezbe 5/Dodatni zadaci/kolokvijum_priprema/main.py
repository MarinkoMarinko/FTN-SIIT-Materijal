# Priprema za kolokvijum
def read_balance():
    accounts = {}
    with open("bank_log.txt", "r") as file:
        for line in file:
            data = line.split()
            if "newaccount" in data[1]:
                accounts[data[0]] = 0
            elif "income" in data[1]:
                accounts[data[0]] += int(data[2])
            else:
                accounts[data[0]] -= int(data[2])
    return accounts
def find_acc(name):
    accounts = read_balance()
    if name in accounts:
        return name + ": " + str(accounts[name])
def wealthiest_acc():
    accounts = read_balance()
    max_name = ""
    max_balance = 0
    for name, balance in accounts.items():
        if balance > max_balance:
            max_balance = balance
            max_name = name
    return max_name
def read_income():
    accounts = {}
    with open("bank_log.txt", "r") as file:
        for line in file:
            data = line.split()
            if "newaccount" in data[1]:
                accounts[data[0]] = 0
            elif "income" in data[1]:
                accounts[data[0]] += 1
    return accounts
def most_income():
    accounts = read_income()
    max_name = ""
    max_income = 0
    for name, income in accounts.items():
        if income > max_income:
            max_income = income
            max_name = name
    return max_name
def acc_less(amount):
    all_accounts = read_balance()
    filtered_accs = {}
    for name, balance in all_accounts.items():
        if balance < amount:
            filtered_accs[name] = balance
    return filtered_accs
def accs_by_name(text):
    all_accounts = read_balance()
    accs = {}
    for name, balance in all_accounts.items():
        if text.lower() in name.lower():
            accs[name] = balance
    return accs
def print_accs(accounts):
    for name, balance in accounts.items():
        print(f"{name}: {balance}")
if __name__ == "__main__":
    name = input("Unesite korisnika: ").strip()
    account = find_acc(name)
    if account:
        print(account)
    else:
        print("Uneti korisnik ne postoji!")
    print("Korisnik sa najvise novca na racunu je:", wealthiest_acc())
    print("Korisnik sa najvise uplata je:", most_income())
    amount = eval(input("Unesite iznos: "))
    filtered_accs = acc_less(amount)
    if len(filtered_accs) == 0:
        print(f"Ne postoje korisnici sa manje novca od {amount}.")
    else:
        print(f"Korisnici sa manje novca od {amount}:")
        print_accs(filtered_accs)
    text = input("Unesite tekst: ")
    matched_accs = accs_by_name(text)
    if len(matched_accs) == 0:
        print(f"Ne postoje korisnici cija imena sadrze rec {text}.")
    else:
        print(f"Korisnici koji sadrze '{text}':")
        print_accs(matched_accs)
    all_accs = read_balance()
    if all_accs:
        print("SVI KORISNICI:")
        print_accs(all_accs)
    else:
        print("Nema prijavljenih korisnika!")