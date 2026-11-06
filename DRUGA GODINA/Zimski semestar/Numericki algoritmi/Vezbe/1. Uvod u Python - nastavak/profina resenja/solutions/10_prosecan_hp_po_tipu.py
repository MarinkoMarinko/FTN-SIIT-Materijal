import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('pokemon_data.csv')

    proseci = df.groupby('Type 1')['HP'].mean()
    print('Broj tipova:', len(proseci))
    print(proseci.idxmax(), round(proseci.max(), 2))
