import os
import pandas as pd

from handle_inputs import handle_mbank, handle_pekao, handle_san

input_dir = os.path.join(os.getcwd(), "INPUTS")
output_dir = os.path.join(os.getcwd(), "OUTPUTS")
input_list = os.listdir(input_dir)

# LOAD DATA
print("AVAILABLE INPUTS:")
for ind, file in enumerate(input_list):
    print(f"{ind} - {file}")

list_choice = int(input("\nSelect file by number: \n"))

input = os.path.join(input_dir, input_list[list_choice])
df = pd.read_csv(input, sep=";")


def main():
    if "pekao" in input:
        handle_pekao(df)
    elif "san" in input:
        handle_san(df)
    elif "san" in input:
        handle_mbank(df)
    else:
        df = pd.DataFrame()
        print("Input not yet supported")

    print(df.columns)
    print(df.head())

    output = input.replace("INPUTS", "OUTPUTS").replace(".csv", ".xlsx")
    df.to_excel(output, header=False, index=False)


if __name__ == "main":
    main()
