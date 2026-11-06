import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    df = pd.read_csv('pokemon_data.csv')

    plt.plot(df['Attack'], df['Defense'], 'o')
    plt.xlabel('Attack')
    plt.ylabel('Defense')
    plt.title('Napad i odbrana pokemona')
    plt.show()
