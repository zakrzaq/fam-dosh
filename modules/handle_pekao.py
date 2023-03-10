def handle_pekao(input_file):
    import pandas as pd  # type: ignore
    
    df = pd.read_csv(input_file, sep=";")
    
    df = df.drop(
        [
            "Data waluty",
            "Waluta",
            "Rachunek źródłowy",
            "Rachunek docelowy",
            "Typ operacji",
        ],
        axis=1,
    )
    df["Data księgowania"] = df["Data księgowania"].apply(lambda x: x.replace(".", "/"))
    df["Kwota operacji"] = df["Kwota operacji"].apply(
        lambda x: x.replace(" ", "").replace(",", ".")
    )

    df = df[
        [
            "Numer referencyjny",
            "Data księgowania",
            "Nadawca / Odbiorca",
            "Adres nadawcy / odbiorcy",
            "Tytułem",
            "Kwota operacji",
            "Kategoria",
        ]
    ]

    df.columns = ["id", "date", "receiver", "address", "title", "amount", "category"]

    return df
