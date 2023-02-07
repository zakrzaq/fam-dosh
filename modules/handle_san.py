def handle_san(input_file):
    import pandas as pd  # type: ignore

    
    df = pd.read_csv(input_file, sep=";")
    
    df = df.iloc[:, [0, 2, 3, 4, 5]]


    df.columns = ["date", "title", "receiver", "address",  "amount"]
    df['id'] = df['date'] + '_' + df['amount'].str.replace('-', '') + '_' + df['title'].str[:25]
    df['category'] = ''
    df['amount'] = df['amount'].str.replace(',', '.')

    df = df[["id", "date", "receiver", "address", "title", "amount", "category"]]

    return df
