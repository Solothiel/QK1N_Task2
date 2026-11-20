from duplicate_removal import remove_duplicates
from descriptive_statistics import calculate_state_statistics
from debt_to_income import debt_to_income_ratio
from negative_equity import identify_negative_equity

if __name__ == "__main__":

    # Load, clean, and remove duplicate data
    cleaned_data, business_id, state, numeric_variables = remove_duplicates()

    #print("\n--- DATA CLEANING TEST RESULTS ---")

    # Check number of records
    #print("\nNumber of records:", len(cleaned_data))

    # Check column data types
    #print("\nData types:")
    #print(cleaned_data[numeric_variables].dtypes)

    # Check missing values
    #print("\nMissing values:")
    #print(cleaned_data.isnull().sum())

    # Check for remaining duplicates
    #print("\nRemaining duplicate rows:")
    #print(cleaned_data.duplicated().sum())

    # Display descriptive statistics
    #print("\nDescriptive statistics:")
    #print(cleaned_data[numeric_variables].describe())

    # Display first five records
    #print("\nFirst five cleaned records:")
    #print(cleaned_data.head())

    #print("\nData cleaning test completed successfully.")

    #print("\n--- STATE STATISTICS TEST RESULTS ---")

    # Calculate descriptive statistics by state
    #state_statistics = calculate_state_statistics(
        #cleaned_data,
        #state,
        #numeric_variables
    #)

    # Display state statistics
    #print("\nState statistics:")
    #print(state_statistics.head())

    # Verify results
    #print("\nNumber of states:", len(state_statistics))

    #print("\nState statistics columns:")
    #print(state_statistics.columns.tolist())

    #print("\nState statistics test completed successfully.")

    #print("\n--- DEBT-TO-INCOME TEST RESULTS ---")

    # Calculate Debt-to-Income
    #cleaned_data = debt_to_income_ratio(cleaned_data)

    # Display Debt-to-Income results
    #print("\nDebt-to-Income:")
    #print(cleaned_data[
              #["Business ID", "Total Long-term Debt",
               #"Total Revenue", "Debt-to-Income"]
          #].head())

    # Check missing values
    # print("\nMissing Debt-to-Income values:")
    #print(cleaned_data["Debt-to-Income"].isnull().sum())

    #print("\nDebt-to-Income test completed successfully.")

    #print("\n--- NEGATIVE EQUITY TEST RESULTS ---")

    # Identify businesses with negative equity
    negative_debt_equity = identify_negative_equity(cleaned_data)

    # Display number of businesses identified
    print("\nBusinesses with negative equity:")
    print(len(negative_debt_equity))

    # Display first five businesses
    print("\nFirst five businesses with negative equity:")
    print(negative_debt_equity.head())

    print("\nNegative equity test completed successfully.")