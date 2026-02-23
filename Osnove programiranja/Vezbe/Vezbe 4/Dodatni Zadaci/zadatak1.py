if __name__ == "__main__":
    while True:
        text = input("Ulaz: ")
        text_len = len(text)
        if text_len <= 7 or text_len % 2 == 0:
            print("Pogresan unos. Pokusajte ponovo.")
            continue
        break
    half = int(text_len / 2)
    print("Izlaz: ", text[half - 1 : half + 2])