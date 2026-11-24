# Step 2 → duplicate removal checks for duplicates and removes them.


def remove_duplicates(raw_data):

    duplicates = raw_data[raw_data.duplicated()]

    if not duplicates.empty:
        raw_data = raw_data.drop_duplicates()
        print(f"Duplicate rows removed.")

    else:
       print(f"No duplicates found.")

    return raw_data


