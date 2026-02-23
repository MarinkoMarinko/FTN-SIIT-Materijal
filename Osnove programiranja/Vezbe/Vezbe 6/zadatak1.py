def workersFee(fee):
    with open("radnici.txt", "r") as file:
        for line in file.readlines():
            data = line.split("|")
            print("Ime: ", data[0])
            hours = sum(float(hour) for hour in data[1:])
            weekly_fee = hours * fee
            if hours > 40:
                weekly_fee *= 1.5
            print("Zarada: ", weekly_fee)
if __name__ == "__main__":
    fee = eval(input("Unesite zaradu po satu: "))
    workersFee(fee)