import os
import pandas as pd

input = os.path.join('jz-pekao-cur-2023-01.csv')

df = pd.read_csv(input, sep=';')

df = df.drop(['Data waluty', 'Waluta', 'Rachunek źródłowy', 'Rachunek docelowy', 'Typ operacji'], axis=1)
df['Data księgowania'] = df['Data księgowania'].apply(lambda x: x.replace('.', '/'))
df['Kwota operacji'] = df['Kwota operacji'].apply(lambda x: x.replace(' ', '').replace(',', '.'))

df = df[['Numer referencyjny', 'Data księgowania', 'Nadawca / Odbiorca', 'Adres nadawcy / odbiorcy', 'Tytułem', 'Kwota operacji', 'Kategoria']]

print(df.columns)
print(df.head(10))

output = input[:-4] + '.xlsx'
df.to_excel(output ,header=False, index=False)
