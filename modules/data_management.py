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

def view_transactions_by_date(df):
    transactions_days = df
    transactions_days['Date'] = pd.to_datetime(transactions_days['Date'])

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
        

# add_a_transaction
def add_transaction(df):
    add_transactions = df
    add_transactions['Date'] = pd.to_datetime(add_transactions['Date'])
    # Prompt for transaction details
    date_str = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Rent): ")
    description = input("Enter a description: ")
    amount = input("Enter the amount: ")

    try:
        # Convert date and amount to appropriate data types
        date = pd.to_datetime(date_str).date()
        amount = float(amount)

        # Create a new transaction row
        new_transaction = pd.DataFrame([[date, category, description, amount]])
        transactions = pd.concat([add_transaction, new_transaction])

        print("Transaction added successfully!")
    except ValueError:
        print("Error: Invalid date or amount format. Please try again.")


# Sample usage
print(add_transaction)

# edit_a_transaction

# delete_a_transaction


