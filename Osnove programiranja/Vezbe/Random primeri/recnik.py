# Program koji ispisuje sve reci koje se pojavljuju u tekst.txt i ispisuje broj pojavljivanja

def read_file():
    with open("tekst.txt", "r", encoding="utf-8") as file:
        return file.read() 
def remove_signs(text: str):
    for ch in ",./?!><[]@#$%^&*()_+-*\"'":
        text = text.replace(ch, "")
    return text
def form_dictionary(dictionary: dict, text: str):
    words = text.split()
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
def print_dictionary(dictionary: dict):
    for key, value in sorted(dictionary.items(), key=lambda item: item[1], reverse=True):
        print(f"{key:<20} {value:>5}")
if __name__ == "__main__":
    text = read_file()
    text = text.lower()
    text = remove_signs(text)
    dictionary = {}
    form_dictionary(dictionary, text)
    print_dictionary(dictionary)