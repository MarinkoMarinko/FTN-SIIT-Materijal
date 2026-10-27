def je_palindrom(s):
    i, j = 0, len(s) - 1
    while i < j:
        while not s[i].isalpha() and i < j:
            i += 1
        while not s[j].isalpha() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1
    return True

if __name__ == "__main__":
    s = "Ana voli Milovana"
    print(je_palindrom(s))