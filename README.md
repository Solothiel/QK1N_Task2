#QKN1 Task 2: Program Implementation (Part 2)



##Project Overview:
	I used Pycharm community edition, to build out the code. I used the flowchart from Task 1 as well as the pseudo code to build. 
	
	
###Technologies	
Python = 3.13
Pandas = 3.1.1
OpenPyXL
PyCharm 2025.1.6.2 (Community Edition)
Excel (.xlsx)
	
###Requirements (found in requirements.txt)
pandas
openpyxl

`pip install pandas openpyxl`

###Dataset:
QK1N Program dataset.xlsx

	
##Structure:
QK1N_Task2
│
├── main.py
├── dataload.py
├── duplicate_removal.py
├── descriptive_statistics.py
├── negative_equity.py
├── debt_to_income.py
├── insert_dti.py
└── README.md

##Structure breakdown	→ Program Processing
main.py  				→ runs the program
dataload 				→ Step 1. loads the dataset and identifies variables
duplicate_removal 		→ Step 2. Removes any exact duplicate business.
descriptive_statistics	→ Step 3. Calculates Mean, Max, Min, and Median for States.
negative_equity			→ Step 4. identifies business with negtative Debt to Equity.
debt_to_income 			→ Step 5. address division-by-zero and calculates debt to income ratio.
insert_dti				→ Step 6. inserts debt to income results into raw_data. 


##NOTES:
Excel column names must match
Duplicates only removes exact duplicates.
Missing financial data isn't excluded from the descriptive_statistics so those values for revenue might not be correct.
Business with zero value in revenue, are giving a NaN, this is only to prevent the division-by-zero error.
The program only displays the results as exporting was not a requirement.



