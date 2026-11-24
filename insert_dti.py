# Step 6 taking the results and adding the debt to income column and populating form step 5.

def insert_debt_to_income(raw_data, debt_to_income):

    raw_data["Debt to Income"] = debt_to_income

    return raw_data