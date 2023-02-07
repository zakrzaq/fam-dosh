def handle_pekao(df):
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

    return df
