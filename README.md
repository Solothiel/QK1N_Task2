# **QKN1 Task 2: Program Implementation (Part 2)**



## **Project Overview:**
	I used Pycharm community edition, to build out the code. I used the flowchart from Task 1 as well as the pseudo code to build. I didn't include part 1 doc file, but i did add the flowchart.

# **RESULTS**

Financial Data successfully loaded to raw_data.
Financial Data successfully loaded to raw_data.
ACTUAL EXCEL COLUMNS:
['Business ID', 'Business State', 'Total Long-term Debt', 'Total Equity', 'Debt to Equity', 'Total Liabilities', 'Total Revenue']
NUMERIC VARIABLES:
['Total Long-term Debt', 'Total Equity', 'Debt to Equity', 'Total Liabilities', 'Total Revenue']
No duplicates found.

Financial Analysis Complete.
   Business ID Business State  ...  Total Revenue  Debt to Income
0    422282013        Alabama  ...      137344716        0.038691
1   2775952013        Alabama  ...     1256317000        1.069367
2   2775952026        Alabama  ...              0             NaN
3   9445082013        Arizona  ...      215580000        0.301920
4   7982872013       Arkansas  ...      402813000        0.174687

[5 rows x 8 columns]

Businesses with Negative Equity:
     Business ID Business State  ...  Total Liabilities  Total Revenue
11    9323722013     California  ...         30048000.0       37782000
13   11245242013     California  ...          3819000.0        1100539
78   14535932013        Montana  ...         32720000.0       33073414
105  14639722013       New York  ...         15900000.0        2389053
111    934562013           Ohio  ...        592174000.0      719783000

[5 rows x 7 columns]

State-Level Statistis:
  Business State Total Long-term Debt  ...                       
                                 mean  ...        min         max
0        Alabama         4.496427e+08  ...          0  1256317000
1        Arizona         6.508800e+07  ...  215580000   215580000
2       Arkansas         8.960450e+07  ...  402813000   555005000
3     California         3.273964e+07  ...    1100539   276869000
4       Colorado         8.470025e+07  ...    7616000   696473000

[5 rows x 21 columns]

Process finished with exit code 0



### Technologies
* **Language:** Python `3.13`
* **Libraries:** 
  * `pandas` (`3.1.1`) — Data manipulation and analysis
  * `openpyxl` — Reading and writing Excel files
  * `numpy` (`2.5.5`) — Supports nmathematical and numerical operations 
* **Data Format:** Microsoft Excel (`.xlsx`)
* **IDE:** PyCharm `2025.1.6.2` (Community Edition)

	
### Requirements (found in requirements.txt)
   pandas
   openpyxl
   numpy

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
   * Excel column names must match
   * Duplicates only remove exact duplicates.
   * Missing financial data isn't excluded from the descriptive_statistics so those values for revenue might not be correct.
   * Businesses with zero value in revenue are given a NaN. This is only to prevent the division-by-zero error.
   * The program only displays the results as exporting was not a requirement.
   * The sequence of processes is per the course even though logically it should be different
   * Stage 2. Should be the cleaning process (duplicate removal and removing of 0 in revenue)
   * Stage 3. Should be generation of the debt to income ratio.
   * Stage 4. Should be the addition of debt to income column with data
   * Stage 5. Should be Negative Value (interchangeable with 6)
   * Stage 6. Should be the Descriptive Statistics, which would include the debt to income.



