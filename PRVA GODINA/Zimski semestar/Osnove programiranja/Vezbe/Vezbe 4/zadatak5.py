if __name__ == "__main__":
    users = open("users.txt", "r")
    bills = open("racuni.txt", "r")
    with open("statistika.txt", "w") as stats:
        stats.write("")
    lines = []
    for line in users.readlines():
        name = line.split("|")[0]
        bill_array = bills.readline().split("|")
        s = sum(float(bill) for bill in bill_array)
        lines.append(f"{name}|{s}|{s / len(bill_array):.2f}")

    with open("statistika.txt", "w") as stats:
        stats.write("\n".join(lines))