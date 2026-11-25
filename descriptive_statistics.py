# Step 3 state_statistics Calculated descriptive statistics
# had to Remove the For loop to match the flowchart and pseudocode.
#switched to a Pandas group by and aggregation operation.

def calculate_state_statistics(raw_data,state, numeric_variables):

    # Groups businesses by state.
    state_groups = raw_data.groupby(state)

    # calculate the descriptive statistics
    statistics_summary = state_groups[numeric_variables].agg(
        ["mean", "median", "min", "max"]
    )

    # store results in new Dataframe
    state_statistics = statistics_summary.reset_index()

    return state_statistics

