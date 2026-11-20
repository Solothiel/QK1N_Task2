# Step 6 taking the results and exporting the updated dataframe.

import pandas as pd
from pathlib import Path




def export_data(raw_data):
    #exports completed results of the dataset.
    output_folder = Path("output")
    output_folder.mkdir(exist_ok=True)

    raw_data.to_csv("output/financial_analysis.csv", index=False)

    print(f"Financial analysis successfully exported")

