# Personal Finance Tracker App

## About the Project
This project involves creating an interactive, text-based Personal Finance Tracker
App that helps users manage and analyze their spending habits.
Users can import a CSV file containing transaction data, perform operations like viewing, adding,
editing, and deleting transactions, and analyze spending patterns.
The app also includes data visualization capabilities, displaying monthly spending trends and
top spending categories.

## Getting started
1. Clone this repository
```
git clone https://github.com/DanaNu1108/Final-Project.git
```

2. Install libraries
```
pip install -r requirements.txt
```

3. Run main.py
```
python main.py
```

## Architecture
There are four modules.
data_management.py, data_analysis.py, data_visualization.py, and file_transfer_management.py.
The main.py has the main logic which calls the function in each modules based on the user input.

#### Data Management(data_management.py)
Handles viewing, adding, editing, and deleting transactions.
- View All Transactions
- View Transactions by Date Range
- Add a Transaction
- Edit a Transaction
- Delete a Transaction

#### Data Analysis(data_analysis.py)
Includes spending analysis by category, average monthly spending, and identifying the top spending category.
- Analyze Spending by Category
- Calculate Average Monthly Spending
- Show Top Spending Category

#### Data Visualization(data_visualization.py)
Creates line, bar, and pie charts to visualize spending trends and distribution.
- Visualize Monthly Spending Trend
- Visualize Spending By Category
- Visualize Percentage Distribution

#### File Transfer Management(file_transfer_management.py)
Imports and exports a csv file
- Import a csv file
- Save Transactions to CSV

## How it works
#### Start the program (Run main.py)
*Note: First of all, It's necessary to import a csv file before using any feature.*
```
=== Personal Finance Tracker ===
Select file number to import.
0. sampledata.csv
Enter the file number: 
```
*After importing a file, the user can see all of the features*
```
'sampledata.csv' has been imported successfully.

=== Personal Finance Tracker ===
0. Import a CSV File
1. View All Transactions
2. View Transactions by Date Range
3. Add a Transaction
4. Edit a Transaction
5. Delete a Transaction
6. Analyze Spending by Category
7. Calculate Average Monthly Spending
8. Show Top Spending Category
9. Visualize Monthly Spending Trend
10. Visualize Spending By Category
11. Visualize Percentage Distribution
12. Save Transactions to CSV
13. Exit
Choose an option (0 - 13):
```

#### Import a CSV File
*The user can select a file existing in the "csv_files" directory.*
```
...
13. Exit
Choose an option (0 - 13): 0

Select file number to import.
0. sampledata.csv
Enter the file number: 0

'sampledata.csv' has been imported successfully.

=== Personal Finance Tracker ===
0. Import a CSV File
1. View All Transactions
...
```

#### View All Transactions
```
...
13. Exit
Choose an option (0 - 13): 1
--- All Transactions ---
          Date   Category        Description   Amount     Type
0   2024-10-01       Food            Grocery    50.75  Expense
1   2024-10-02       Rent       Monthly Rent  1200.00  Expense
2   2024-10-02  Utilities   Electricity Bill    60.00  Expense
3   2024-10-03       Food             Dinner    30.00  Expense
4   2024-10-04  Transport         Bus Ticket     2.75  Expense
5   2024-10-05       Food          Breakfast    15.00  Expense
...
```

#### View Transactions by Date Range
```
...
13. Exit
Choose an option (0 - 13): 2

Enter the start date (YYYY-MM-DD): 2024-10-02
Enter the end date (YYYY-MM-DD): 2024-10-04
--- Transactions from 2024-10-02 to 2024-10-04 ---
      Date  Category      Description  Amount    Type
2024-10-02      Rent     Monthly Rent 1200.00 Expense
2024-10-02 Utilities Electricity Bill   60.00 Expense
2024-10-03      Food           Dinner   30.00 Expense
2024-10-04 Transport       Bus Ticket    2.75 Expense

=== Personal Finance Tracker ===
0. Import a CSV File
1. View All Transactions
...
```

#### Add a Transaction
```
...
13. Exit
Choose an option (0 - 13): 3

Enter the date (YYYY-MM-DD): 2024-10-31
Enter the category (e.g., Food, Rent): 2024-10-31
Enter a description: dummy
Enter the amount: 2000
Enter transaction type Expense(1) or Income(2): 1
Transaction added successfully!

=== Personal Finance Tracker ===
0. Import a CSV File
...
```

#### Edit a Transaction
```
...
13. Exit
Choose an option (0 - 13): 4

Enter the index of the transaction to edit: 0
Current Transaction Details:
Date: 2024-10-01
Category: Food
Description: Grocery
Amount: 50.75
Enter new date (YYYY-MM-DD) or press Enter to keep current: 2024-10-02
Enter new category or press Enter to keep current: 
Enter new description or press Enter to keep current: 
Enter new amount or press Enter to keep current: 60.50
Transaction updated successfully!

=== Personal Finance Tracker ===
0. Import a CSV File
1. View All Transactions
...
```

#### Delete a Transaction
```
...
13. Exit
Choose an option (0 - 13): 5

Enter the index of the transaction to delete: 0
Transaction deleted successfully!

=== Personal Finance Tracker ===
0. Import a CSV File
1. View All Transactions
...
```

#### Analyze Spending by Category
```
...
13. Exit
Choose an option (0 - 13): 6

 -> SPENDING BY CATEGORY  
| Category   |   Total Spending |
|:-----------|-----------------:|
| Food       |           150    |
| Rent       |          2400    |
| Transport  |            27.75 |
| Utilities  |           100    |
| Total      |          2677.75 |

=== Personal Finance Tracker ===
0. Import a CSV File
1. View All Transactions
...
```

#### Calculate Average Monthly Spending
```
...
13. Exit
Choose an option (0 - 13): 7

 -> AVERAGE MONTHLY SPENDING  
| Month         |   Expense |   Income |
|:--------------|----------:|---------:|
| (2024, 'Oct') |   267.775 |      900 |

=== Personal Finance Tracker ===
0. Import a CSV File
1. View All Transactions
...
```

#### Show Top Spending Category
```
...
13. Exit
Choose an option (0 - 13): 8

 - TOP SPENDING CATEGORY - 
| Category   |   Amount |
|:-----------|---------:|
| Rent       |     2400 |

=== Personal Finance Tracker ===
0. Import a CSV File
1. View All Transactions
...
```
#### Visualize Monthly Spending Trend
*Shows a line chart*

#### Visualize Spending By Category
*Shows a bar chart*

#### Visualize Percentage Distribution
*Shows a pie chart*

#### Save Transactions to CSV
```
...
13. Exit
Choose an option (0 - 13): 12

Enter file name to save (e.g., 'transactions.csv'): save_test.csv

Transactions saved to 'save_test.csv' successfully!

=== Personal Finance Tracker ===
0. Import a CSV File
1. View All Transactions
...
```


#### Exit
```
...
13. Exit
Choose an option (0 - 13): 13

Exiting the Personal Finance Tracker. Goodbye!
```