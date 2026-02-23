def isPalindrom(text, start, end):
    if start >= end:
        return True
    elif text[start] != text[end]:
        return False
    return isPalindrom(text, start + 1, end - 1)
if __name__ == "__main__":
    while True:
        text = input("Unesite string: ").strip().lower()
        if len(text) == 0:
            print("Morate uneti neki tekst!")
            continue
        print("Palindrom? ", isPalindrom(text, 0, len(text) - 1))