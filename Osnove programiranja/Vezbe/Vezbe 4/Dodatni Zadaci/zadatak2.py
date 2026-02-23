if __name__ == "__main__":
    str1 = "Lampica"
    str2 = "Kokos"
    str1_half = int(len(str1) / 2)
    str2_half = int(len(str2) / 2)
    result = str1[0] + str2[0] + str1[str1_half] + str2[str2_half] + str1[-1] + str2[-1]
    print(result)