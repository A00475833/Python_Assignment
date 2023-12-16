import pandas as pd


df = pd.read_csv('data/titles.csv')


def countVowels(t):
    t = str(t).lower()
    return sum(map(t.count, ['a', 'e', 'i', 'o', 'u']))


df['vowels'] = df.apply(lambda row: countVowels(row['title']), axis=1)


print(df)
