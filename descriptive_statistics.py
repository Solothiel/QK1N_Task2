# Step 4 state_statistics  Calculated descriptive statistics


import pandas as pd
from pathlib import Path
from duplicate_removal import remove_duplicates

def calculate_state_statistics(raw_data,state, numeric_variables):

    # Groups businesses by state.
    state_groups = raw_data.groupby(state)

    #creates an empty list for the descriptive statistics (mean,medium, min, and max)
    statistics_summary = []

    # calculate the descriptive statistics for each state.
    for state_name, current_group in state_groups:
        state_metrics = {"State": state_name}
        for variable in numeric_variables:
            values = current_group[variable].dropna()
            state_metrics[variable + "_mean"] = values.mean()
            state_metrics[variable + "_median"] = values.median()
            state_metrics[variable + "_min"] = values.min()
            state_metrics[variable + "_max"] = values.max()

        statistics_summary.append(state_metrics)

    # store results in new Dataframe
    state_statistics = pd.DataFrame(statistics_summary)

    output_folder = Path("output")
    output_folder.mkdir(exist_ok=True)


    # Export statistics to CSV
    state_statistics.to_csv("output/state_statistics.csv", index=False)

    print("State statistics successfully calculated.")
    return state_statistics

