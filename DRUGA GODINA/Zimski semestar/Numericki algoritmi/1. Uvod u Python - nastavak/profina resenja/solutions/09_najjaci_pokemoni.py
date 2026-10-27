import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('pokemon_data.csv')

    kolone = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
    df['Total'] = df[kolone].sum(axis=1)
    najjaci = df.nlargest(5, 'Total')
    print(najjaci[['Name', 'Total']])
