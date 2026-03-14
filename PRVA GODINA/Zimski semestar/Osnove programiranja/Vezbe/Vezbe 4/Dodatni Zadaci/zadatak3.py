if __name__ == "__main__":
    str1 = "3215ABCde7fAg"
    numbers = 0
    sm_letters = 0
    for letter in str1:
        if letter.isdigit():
            numbers += 1
        elif letter.islower():
            sm_letters += 1
    print("Broj cifara: ", numbers)
    print("Broj malih slova: ", sm_letters)