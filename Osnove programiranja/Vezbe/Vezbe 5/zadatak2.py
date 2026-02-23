def karakteristikeNiza(numbers):
    print("Najveci element niza je: ", max(numbers))
    print("Najmanji element niza je: ", min(numbers))
    print("Suma elemenata niza je: ", sum(numbers))
    print(f"Prosek elemenata niza je: {sum(numbers) / len(numbers):.2f}")
if __name__ == "__main__":
    numbers = []
    while True:
        text = input("Unesite broj, a za prekid unosa unesite x: ")
        if(text.lower() == "x"):
            break
        numbers.append(eval(text))
    karakteristikeNiza(numbers)