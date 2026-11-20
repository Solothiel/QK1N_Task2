import pandas as pd
from duplicate_removal import remove_duplicates
def debt_to_income_ratio(raw_data):

    #create any empty column "Debt-to-Income"
    raw_data["Debt-to-Income"] = None

    # check to if total revenue is zero and calculate "Debt-to-Income"
    for index, business in raw_data.iterrows():
        if business["Total Revenue"] == 0:
            raw_data.loc[index, "Debt-to-Income"] = None

        else:
            raw_data.loc[index, "Debt-to-Income"] = (
                business["Total Long-term Debt"] / business["Total Revenue"]
            )


    return raw_data


