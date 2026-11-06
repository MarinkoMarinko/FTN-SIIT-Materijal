import pandas as pd
import matplotlib.pyplot as plt

from z1 import fit
from z2 import make_predictions

if __name__ == "__main__":
    df = pd.read_csv("../data/skincancer.csv")

    plt.figure(figsize=(12, 5))

    df_lat = df.sort_values("Lat")
    x = df_lat["Lat"].tolist()
    y = df_lat["Mort"].tolist()

    slope, intercept = fit(x, y)
    y_pred = make_predictions(x, slope, intercept)

    plt.subplot(1, 2, 1)
    plt.scatter(x, y)
    plt.plot(x, y_pred, color="red", label="Predikcije")
    plt.xlabel("Geografska sirina")
    plt.ylabel("Stopa smrtnosti")
    plt.title("Geografska sirina")

    df_long = df.sort_values("Long")
    x = df_long["Long"].tolist()
    y = df_long["Mort"].tolist()

    slope, intercept = fit(x, y)
    y_pred = make_predictions(x, slope, intercept)

    plt.subplot(1, 2, 2)
    plt.scatter(x, y)
    plt.plot(x, y_pred, color="red")
    plt.xlabel("Geografska duzina")
    plt.ylabel("Stopa smrtnosti")
    plt.title("Geografska duzina")

    plt.tight_layout()
    plt.show()