import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../pokemon_data.csv")

    df["Odnos"] = (df["Attack"] / df["Defense"]).round(2)

    df.drop(columns=["Generation"], inplace=True)

    print(df.head())

    print("-----------------------------------------------------------------------------------------\n")
    print(df[df["Odnos"] == df["Odnos"].max()])