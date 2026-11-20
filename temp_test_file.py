from duplicate_removal import remove_duplicates


if __name__ == "__main__":

    # Load, clean, and remove duplicate data
    cleaned_data, business_id, state, numeric_variables = remove_duplicates()

    print("\n--- DATA CLEANING TEST RESULTS ---")

    # Check number of records
    print("\nNumber of records:", len(cleaned_data))

    # Check column data types
    print("\nData types:")
    print(cleaned_data[numeric_variables].dtypes)

    # Check missing values
    print("\nMissing values:")
    print(cleaned_data.isnull().sum())

    # Check for remaining duplicates
    print("\nRemaining duplicate rows:")
    print(cleaned_data.duplicated().sum())

    # Display descriptive statistics
    print("\nDescriptive statistics:")
    print(cleaned_data[numeric_variables].describe())

    # Display first five records
    print("\nFirst five cleaned records:")
    print(cleaned_data.head())

    print("\nData cleaning test completed successfully.")