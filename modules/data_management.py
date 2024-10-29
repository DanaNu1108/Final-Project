import pandas as pd
from constants import common_error_type_to_error_message


def view_all_transactions(df: pd.DataFrame) -> None:

    if df is None:
        print(common_error_type_to_error_message["NO_FILE_IMPORTED"])
        return

    print("--- All Transactions ---")
    print(df)

    return

#2. View Transactions by Date Range
from datetime import datetime

transactions_days = pd.DataFrame({
    'Date': ['2024-10-02', '2024-10-02', '2024-10-03', '2024-09-30'],
    'Category': ['Rent', 'Utilities', 'Food', 'Groceries'],
    'Description': ['Monthly Rent', 'Electricity Bill', 'Dinner', 'Weekly Groceries'],
    'Amount': [1200.0, 60.0, 30.0, 100.0]
})
transactions_days['Date'] = pd.to_datetime(transactions_days['Date'])

def view_transactions_by_date():

    start_date_begin = input("Enter the start date (YYYY-MM-DD): ")
    end_date_end = input("Enter the end date (YYYY-MM-DD): ")

    #input to datetime objects
    start_date = pd.to_datetime(start_date_begin)
    end_date = pd.to_datetime(end_date_end)

    # Filter transactions within the date range
    filtered_transactions = transactions_days[(transactions_days['Date'] >= start_date) & (transactions_days['Date'] <= end_date)]

    # Display results message
    if not filtered_transactions.empty:
        print(f"--- Transactions from {start_date_begin} to {end_date_end} ---")
        print(filtered_transactions.to_string(index=False))
    else:
        print("No transactions found in this date range.")
        
view_transactions_by_date()

# add_a_transaction

# edit_a_transaction

# delete_a_transaction


