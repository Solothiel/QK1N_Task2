from dataload import identify_data
from duplicate_removal import remove_duplicates
from debt_to_income import debt_to_income_ratio
from negative_equity import identify_negative_equity
from descriptive_statistics import calculate_state_statistics
from insert_dti import insert_debt_to_income


def main():
    # Step 1 → loading the dataframe with dataset and identifying the columns
    raw_data, business_id, state, numeric_variables = identify_data()

    raw_data, business_id, state, numeric_variables = identify_data()

    print("ACTUAL EXCEL COLUMNS:")
    print(raw_data.columns.tolist())

    print("NUMERIC VARIABLES:")
    print(numeric_variables)

    # Step 2 → looking for and removing any exact duplicates.
    raw_data = remove_duplicates(raw_data)

    # Step 3 → Grouping by state, and calculating the min,max,mean and median for each.
    # Results stored in a dataframe.
    state_statistics = calculate_state_statistics(raw_data, state, numeric_variables)

    # Step 4 → Identifying the business with negative a debt to equity value.
    # saving the identified business to new dataframe.
    negative_equity = identify_negative_equity(raw_data)


    # Step 5 → checking Total Revenue and if zero then setting debt to income to NaN
    # Otherwise calculating normally and saving results to a list.
    debt_to_income = debt_to_income_ratio(raw_data)

    # Step 6 → creating a column and saving the data from Step 5.
    # Uploading the column to raw_data.
    raw_data = insert_debt_to_income(raw_data, debt_to_income)


    print("\nFinancial Analysis Complete.")

    print(raw_data.head())

    print("\nBusinesses with Negative Equity:")
    print(negative_equity.head())

    print("\nState-Level Statistis:")
    print(state_statistics.head())


if __name__ == "__main__":
    main()
