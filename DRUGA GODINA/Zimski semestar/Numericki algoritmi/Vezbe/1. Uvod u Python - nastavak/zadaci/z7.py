import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../pokemon_data.csv")
    print("Legendary pokemons:", (df["Legendary"] == True).sum())
    print("Fire pokemons:", (df["Type 1"] == "Fire").sum())
    print("Gen1 pokemons:", (df["Generation"] == 1).sum())