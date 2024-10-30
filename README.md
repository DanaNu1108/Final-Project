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

#### File Transfer Management(file_transfer_management.py)
Imports and exports a csv file
- Import a csv file
- Save Transactions to CSV

## How it works
#### Run main.py

```
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
10. Save Transactions to CSV
11. Exit
Choose an option (0 - 11): 
```

#### Import a CSV File
*Note: It's necessary to import a csv file before using any other features except for "Exit".*
```
...
11. Exit
Choose an option (0 - 11): 0

Select the file number to import.
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
11. Exit
Choose an option (0 - 11): 1
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
11. Exit
Choose an option (0 - 11): 2

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

#### Edit a Transaction
```
...
11. Exit
Choose an option (0 - 11): 4

Enter the index of the transaction to edit: 0
Current Transaction Details:
Date: 2024-10-01 00:00:00
Category: Food
Description: Grocery
Amount: 50.75
Enter new date (YYYY-MM-DD) or press Enter to keep current: 2024-10-31
Enter new category or press Enter to keep current: Cloth
Enter new description or press Enter to keep current: dummy
Enter new amount or press Enter to keep current: 100
Transaction updated successfully!

=== Personal Finance Tracker ===
0. Import a CSV File
1. View All Transactions
...
```

#### Delete a Transaction
```
...
11. Exit
Choose an option (0 - 11): 5

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
11. Exit
Choose an option (0 - 11): 6

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
11. Exit
Choose an option (0 - 11): 7

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
11. Exit
Choose an option (0 - 11): 8

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

#### Save Transactions to CSV
```
...
11. Exit
Choose an option (0 - 11): 10

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
11. Exit
Choose an option (0 - 11): 11

Exiting the Personal Finance Tracker. Goodbye!
```