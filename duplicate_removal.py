# Step 2 → duplicate removal checks for duplicates and removes them.

#imports the data from step 2
from dataload import identify_data


def remove_duplicates():
    raw_data, business_id, state, numeric_variables = identify_data()

    duplicates = raw_data[raw_data.duplicated()]

    if not duplicates.empty:
        raw_data = raw_data.drop_duplicates()
        print(f"Duplicate rows removed.")

    else:
       print(f"No duplicates found.")

    return raw_data, business_id, state, numeric_variables


