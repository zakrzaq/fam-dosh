def handle_mbank(input_file):
    import pandas as pd  # type: ignore
    # from io import StringIO
    #
    # f = open(input_file, "r")
    # csv = f.readlines()
    # csv = csv[23:]
    #
    #
    # inp = ''
    # for line in csv:
    #     print(line)
    #     inp += line 
    #
    # csv_string = StringIO(inp)


    df = pd.read_csv(input_file, sep=";")

    # print(df.dtypes)
    # # df.columns = ['date', 'title', 'address', 'category', 'amount', 'receiver']
    # for col in df.columns:
    #     df[col] = df[col].astype('string').replace(r'\s+', ' ', regex=True)
    #
    # # df['id'] = df['date'] + '_' + df['amount'] + '_' + df['title'].str[:25]
    # # df['amount'].replace(' ', '').replace(',', '.')
    # # print(df.dtypes)
    df = df[['#Data operacji']]
    return df
