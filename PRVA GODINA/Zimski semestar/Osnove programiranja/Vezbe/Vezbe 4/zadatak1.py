if __name__ == "__main__":
    s1 = input("Unesite prvi string: ").strip()
    s2 = input("Unesite drugi string: ").strip()
    novi = s1[:3] * 2 + s2[-3:]
    print(novi)