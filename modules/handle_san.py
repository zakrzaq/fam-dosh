def handle_san(df):
    df = df.iloc[:, [0, 2, 3, 4, 5]]


    # df.columns = ["id", "date", "receiver", "address", "title", "amount", "category"]

    return df
