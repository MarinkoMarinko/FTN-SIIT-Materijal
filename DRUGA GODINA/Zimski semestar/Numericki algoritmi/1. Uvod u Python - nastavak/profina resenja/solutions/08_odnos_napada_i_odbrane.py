import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('pokemon_data.csv')

    df['Odnos'] = round(df['Attack'] / df['Defense'], 2)
    df = df.drop(columns=['Generation'])
    print(df.head())

    najveci = df.loc[df['Odnos'].idxmax()]
    print(najveci['Name'], najveci['Odnos'])
