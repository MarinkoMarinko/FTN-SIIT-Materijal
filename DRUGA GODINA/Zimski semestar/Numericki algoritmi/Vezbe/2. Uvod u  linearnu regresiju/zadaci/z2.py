def predict(x, slope, intercept):
    return slope * x + intercept

def make_predictions(x, slope, intercept):
    y_pred = [predict(xi, slope, intercept) for xi in x]
    return y_pred