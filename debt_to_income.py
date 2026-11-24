



def debt_to_income_ratio(raw_data):

    # create an empty list
    debt_to_income = []

    # check to if total revenue is zero and calculate "Debt to Income"
    for index, business in raw_data.iterrows():
        #this handles the division-by-zero issue
        if business["Total Revenue"] == 0:
            dti_ratio = float("nan")

        else:
            dti_ratio = (
                business["Total Long-term Debt"] /
                business["Total Revenue"]
            )

    # appends the ratio for each business to list
        debt_to_income.append(dti_ratio)

    return debt_to_income


