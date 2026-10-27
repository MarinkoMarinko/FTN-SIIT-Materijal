def fit(x, y):
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)

    numerator = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y))
    denominator = sum((xi - x_mean) ** 2 for xi in x)

    slope = numerator / denominator
    intercept = y_mean - slope * x_mean

    return slope, intercept

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [20, 30, 40, 50, 60]

    slope, intercept = fit(x, y)

    print(slope)      # 10.0
    print(intercept)  # 10.0