from identify_data import clean_data

if __name__ == "__main__":

    cleaned_data, business_id, state, numeric_variables = clean_data()

    print("\n--- DATA CLEANING TEST RESULTS ---")

    # Check number of records
    print("Number of records:", len(cleaned_data))

    # Check column data types
    print("\nData types:")
    print(cleaned_data[numeric_variables].dtypes)

    # Check missing values
    print("\nMissing values:")
    print(cleaned_data.isnull().sum())

    # Display descriptive statistics
    print("\nDescriptive statistics:")
    print(cleaned_data[numeric_variables].describe())

    # Display first five records
    print("\nFirst five cleaned records:")
    print(cleaned_data.head())

    print("\nData cleaning test completed successfully.")