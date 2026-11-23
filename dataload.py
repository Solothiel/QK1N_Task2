# This is Step 1
# Need to install openpyxl to read Excel files from the Terminal.
# pip install pandas openpyxl

import pandas as pd
from pathlib import Path

def load_data ():
    # this will locate file from the user's downloads folder
    input_file = Path.home() / "Downloads" / "QKN1 Program dataset.xlsx"

    #checks that the file exists
    if not input_file.exists():
        raise FileNotFoundError(f"Could not find the dataset at: {input_file}")

    # loads data to dataframe raw_data.
    raw_data = pd.read_excel(input_file)

    #confirms data is present and loaded.

    if raw_data.empty:
        raise ValueError("The dataset was loaded, but its contains no data.")

    print("Financial Data successfully loaded to raw_data.")

    return raw_data


def clean_data():
    #load raw_data dataframe.
    raw_data = load_data()

    # Identify non financial data
    business_id = "Business ID"
    state = "Business State"

    # Identify the numeric variables
    numeric_variables = [
        "Total Long-term Debt",
        "Total Equity",
        "Debt-to-Equity",
        "Total Liabilities",
        "Total Revenue"
    ]


    return raw_data, business_id, state, numeric_variables





