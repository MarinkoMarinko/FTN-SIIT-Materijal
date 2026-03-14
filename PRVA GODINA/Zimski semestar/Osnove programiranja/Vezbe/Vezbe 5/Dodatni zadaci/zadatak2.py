def sentence(words):
    output = ""
    for word in words:
        output += word + " "
    return output
if __name__ == "__main__":
    words = []
    while True:
        text = input("Unesite rec, x za kraj: ").strip()
        if len(text) == 0:
            print("Morate uneti rec!")
            continue
        elif text.lower() == "x":
            break
        words.append(text)
    print("Rezultat: ", sentence(words))