def format_spaces(text):
    return " ".join(text)
if __name__ == "__main__":
    with open("neformatiranTekst.txt", "r") as file_in, open("formatiranTekst.txt", "w") as file_out:
        title = format_spaces(file_in.readline().split())
        file_out.write(title.title().center(100) + "\n")
        writer = format_spaces(file_in.readline().split())
        file_out.write(writer + "\n")
        for sentence in file_in:
            sentence = format_spaces(sentence.split())
            file_out.write(sentence.ljust(5) + "\n")