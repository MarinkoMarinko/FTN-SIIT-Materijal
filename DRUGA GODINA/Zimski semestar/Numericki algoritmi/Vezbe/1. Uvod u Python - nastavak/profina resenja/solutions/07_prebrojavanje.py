import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('pokemon_data.csv')

    print('Legendarni:', df['Legendary'].sum())
    print('Fire:', (df['Type 1'] == 'Fire').sum())
    print('Prva generacija:', (df['Generation'] == 1).sum())
