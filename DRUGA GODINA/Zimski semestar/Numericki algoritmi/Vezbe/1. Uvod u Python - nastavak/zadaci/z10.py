import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../pokemon_data.csv")

    avg_hp = df.groupby("Type 1")["HP"].mean()
    print("Number of types:", avg_hp.count())
    print("Type with biggest avg HP:", avg_hp.idxmax())