# Step 5. Debt to income calculation using vectorized conditional logic
# originally was for loop but had to change to match flowchart & pseudocode


import numpy as np

def debt_to_income_ratio(raw_data):

    debt_to_income = np.where(
        raw_data["Total Revenue"] == 0,
        np.nan,
        raw_data["Total Long-term Debt"] / raw_data["Total Revenue"]
    )

    return debt_to_income


