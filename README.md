# **QKN1 Task 2: Program Implementation (Part 2)**



## **Project Overview:**
	I used Pycharm community edition, to build out the code. I used the flowchart from Task 1 as well as the pseudo code to build. I didn't include part 1 doc file, but i did add the flowchart.

	
### Technologies
* **Language:** Python `3.13`
* **Libraries:** 
  * `pandas` (`3.1.1`) — Data manipulation and analysis
  * `openpyxl` — Reading and writing Excel files
* **Data Format:** Microsoft Excel (`.xlsx`)
* **IDE:** PyCharm `2025.1.6.2` (Community Edition)

	
### Requirements (found in requirements.txt)
   pandas
   openpyxl

`pip install pandas openpyxl`

> **Dataset:** `QK1N Program dataset.xlsx`

	
## **Structure:**
```
QK1N_Task2/
├── images/
│   └── flowchart.png
├── main.py
├── dataload.py
├── duplicate_removal.py
├── descriptive_statistics.py
├── negative_equity.py
├── debt_to_income.py
├── insert_dti.py
└── README.md
```

## Structure breakdown	→ Program Processing
* **`main.py`** — Runs the full program.
  1. **`dataload.py`**: Loads the dataset and identifies variables.
  2. **`duplicate_removal.py`**: Removes any exact duplicate businesses.
  3. **`descriptive_statistics.py`**: Calculates Mean, Max, Min, and Median for states.
  4. **`negative_equity.py`**: Identifies businesses with negative Debt-to-Equity.
  5. **`debt_to_income.py`**: Addresses division-by-zero and calculates Debt-to-Income ratio.
  6. **`insert_dti.py`**: Inserts Debt-to-Income results into `raw_data`.

 


## NOTES:
   Excel column names must match
   Duplicates only removes exact duplicates.
   Missing financial data isn't excluded from the descriptive_statistics so those values for revenue might not be correct.
   Business with zero value in revenue, are giving a NaN, this is only to prevent the division-by-zero error.
   The program only displays the results as exporting was not a requirement.



