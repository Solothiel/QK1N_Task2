# This is Step 1
# Need to install openpyxl to read Excel files from the Terminal.
# pip install pandas openpyxl
import pandas as pd
from pathlib import path

def load_data ():
    # this will locate file from the user's downloads folder
    input_file = path.home() / "Downloads" / "QKN1 Program dataset.xlsx"

    #checks that the file exists
    IF NOT input_file.exists():
        raise FileNotFoundError(f"Could not find the dataset at: {input_file}")

    # loads data to dataframe raw_data.
    raw_data = pd.read_excel(input_file)

    #confirms data is present and loaded.

    if raw_data.empty:
        raise ValueError("The dataset was loaded, but its contains no data.")

    print("Financial Data successfully loaded to raw_data.")
    print(f"Rows loaded: {raw_data.shape[0]}")
    print(f"Columns loaded: {raw_data.shape[1]}")


