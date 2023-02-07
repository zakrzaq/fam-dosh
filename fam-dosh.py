import os
import pandas as pd # type: ignore

from modules.handle_mbank import handle_mbank 
from modules.handle_pekao import handle_pekao
from modules.handle_san import handle_san

input_dir = os.path.join(os.getcwd(), "INPUTS")
output_dir = os.path.join(os.getcwd(), "OUTPUTS")
input_list = os.listdir(input_dir)



def app():
    # LOAD DATA
    print("AVAILABLE INPUTS:")
    for ind, file in enumerate(input_list):
        print(f"{ind} - {file}")

    list_choice = int(input("\nSelect file by number: \n"))
    input_file = os.path.join(input_dir, input_list[list_choice])
    df = pd.read_csv(input_file, sep=";")

    #PROCESS
    if not df.empty:
        if "pekao" in input_file:
            out = handle_pekao(df)
        elif "san" in input_file:
            out = handle_san(df)
        elif "san" in input_file:
            out = handle_mbank(df)
        else:
            out = pd.DataFrame()
            print("Input not yet supported")

        print(out.columns)
        print(out.head())

        output = input_file.replace("INPUTS", "OUTPUTS").replace(".csv", ".xlsx")
        out.to_excel(output, header=False, index=False)

app()
