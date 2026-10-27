studenti = {"Ana": [10, 9, 8], "Marko": [6, 7, 6], "Ivana": [9, 10, 10], "Jovan": [7, 8, 6]}

prosek = { key: round(sum(val) / len(val), 2) for key, val in studenti.items() }

print(prosek)
print("Najbolji student:", max(prosek, key=lambda x: prosek[x]))
print([ime for ime, prosek in prosek.items() if prosek > 8])