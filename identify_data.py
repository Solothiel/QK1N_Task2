# Step 2  Identify data and assign numeric to financial data.

import pandas as pd
from dataload import load_data


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

    # Verify numeric data types.
    for variable in numeric_variables:
        raw_data[variable] = pd.to_numeric(
            raw_data[variable],
            errors="coerce"
        )
    print("Numeric variables completed")

    return raw_data, business_id, state, numeric_variables