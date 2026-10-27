import pandas as pd
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

if __name__ == "__main__":
    df = pd.read_csv("../pokemon_data.csv")
    plt.scatter(df["Attack"], df["Defense"])

    plt.xlabel("Attack")
    plt.ylabel("Defense")
    plt.title("Attack vs Defense")

    plt.show()