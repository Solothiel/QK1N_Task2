# This is Step 5b and 5c combined.


import pandas as pd



# Identify the businesses who has negative value in the debt-to-equity column.

def identify_negative_equity(raw_data):

    negative_debt_equity = raw_data [
        raw_data["Debt to Equity"] < 0
   ]

    # stores the negative equity business to dataframe
    negative_equity = pd.DataFrame(negative_debt_equity)


    return negative_equity


