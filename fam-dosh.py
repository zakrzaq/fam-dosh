import os
import pandas as pd

input_dir = os.path.join(os.getcwd(), 'INPUTS')
output_dir = os.path.join(os.getcwd(), 'OUTPUTS')
input_list = os.listdir(input_dir)

# LOAD DATA
print('AVAILABLE INPUTS:')
for ind, file in enumerate(input_list):
    print(f"{ind} - {file}")

list_choice = int(input('\nSelect file by number: \n'))

input = os.path.join(input_dir, input_list[list_choice])
df = pd.read_csv(input, sep=';')

# DATA HANDLING
def handle_pekao(df):
    df = df.drop(['Data waluty', 'Waluta', 'Rachunek źródłowy', 'Rachunek docelowy', 'Typ operacji'], axis=1)
    df['Data księgowania'] = df['Data księgowania'].apply(lambda x: x.replace('.', '/'))
    df['Kwota operacji'] = df['Kwota operacji'].apply(lambda x: x.replace(' ', '').replace(',', '.'))

    df = df[['Numer referencyjny', 'Data księgowania', 'Nadawca / Odbiorca', 'Adres nadawcy / odbiorcy', 'Tytułem', 'Kwota operacji', 'Kategoria']]

def handle_san(df):
    df = df.iloc[:, [0, 2, 3, 4, 5]]
    
# RUNTIME
if 'pekao' in input:
    handle_pekao(df)
elif 'san' in input:
    handle_san(df)
else:
    df = pd.DataFrame()
    print('Input not yet supported')

print(df.columns)
print(df.head())

# SAVE
output = input.replace('INPUTS', 'OUTPUTS').replace('.csv', '.xlsx')
df.to_excel(output ,header=False, index=False)
