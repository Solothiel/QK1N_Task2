# This is Step 5b and 5c combined.

from debt_to_income import debt_to_income_ratio
import pandas as pd

from pathlib import Path

# Identify the businesses who has negative value in the debt-to-equity column.

def identify_negative_equity(raw_data):
    # creates an empty list to save the dataframe with the business with negative debt equity.

    negative_debt_equity = []

    # checking each business(iterate).
    for index, business in raw_data.iterrows():

        if pd.notna(business["Debt-to-Equity"]) and business["Debt-to-Equity"] < 0:
            negative_debt_equity.append(business)

    #converts list to Dataframe
    negative_debt_equity = pd.DataFrame(negative_debt_equity)

    #Create output folder if it does not exist.

    output_folder = Path("output")
    output_folder.mkdir(exist_ok=True)

    # Save business with negative equity to CSV
    negative_debt_equity.to_csv(output_folder / "Negative_equity.csv", index=False)


    return negative_debt_equity


