
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("../data/skincancer.csv")

plt.figure(figsize=(12, 5))

df_lat = df.sort_values("Lat")

x = df_lat[["Lat"]]
y = df_lat["Mort"]

model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)

plt.subplot(1, 2, 1)
plt.scatter(x["Lat"], y)
plt.plot(x["Lat"], y_pred, color="red")
plt.xlabel("Geografska širina")
plt.ylabel("Stopa smrtnosti")
plt.title("Geografska širina")

df_long = df.sort_values("Long")

x = df_long[["Long"]]
y = df_long["Mort"]

model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)

plt.subplot(1, 2, 2)
plt.scatter(x["Long"], y)
plt.plot(x["Long"], y_pred, color="red")
plt.xlabel("Geografska dužina")
plt.ylabel("Stopa smrtnosti")
plt.title("Geografska dužina")

plt.tight_layout()
plt.show()