import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../pokemon_data.csv")

    df["Total"] = df["HP"] + df["Attack"] + df["Defense"] + df["Sp. Atk"] + df["Sp. Def"] + df["Speed"]

    print(df.sort_values("Total", ascending=False)[["Name", "Total"]].head(5))