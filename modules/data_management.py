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
    transaction = df
    transaction['Date'] = pd.to_datetime(transaction['Date'])
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

        # Append to the DataFrame
        global transactionist
        transactions = pd.concat([transaction, new_transaction], ignore_index=True)

        print("Transaction added successfully!")
    except ValueError:
        print("Error: Invalid date or amount format. Please try again.")

# edit_a_transaction

def edit_transaction(df):
    edit_transactions = df
    edit_transactions['Date'] = pd.to_datetime(edit_transactions['Date'])
    try:
        index = int(input("Enter the index of the transaction to edit: "))

        # Check if the index is valid
        if index not in edit_transactions.index:
            print("Invalid index.")
            return

        # Display current transaction details
        print("Current Transaction Details:")
        print(f"Date: {edit_transactions.at[index, 'Date']}")
        print(f"Category: {edit_transactions.at[index, 'Category']}")
        print(f"Description: {edit_transactions.at[index, 'Description']}")
        print(f"Amount: {edit_transactions.at[index, 'Amount']}")

        # Prompt for new values or press Enter to keep current
        new_date = input("Enter new date (YYYY-MM-DD) or press Enter to keep current: ")
        new_category = input("Enter new category or press Enter to keep current: ")
        new_description = input("Enter new description or press Enter to keep current: ")
        new_amount = input("Enter new amount or press Enter to keep current: ")

        # Update transaction if a new value is provided
        if new_date:
            edit_transactions.at[index, 'Date'] = pd.to_datetime(new_date).date()
        if new_category:
            edit_transactions.at[index, 'Category'] = new_category
        if new_description:
            edit_transactions.at[index, 'Description'] = new_description
        if new_amount:
            edit_transactions.at[index, 'Amount'] = float(new_amount)

        print("Transaction updated successfully!")
    except ValueError:
        print("Error: Invalid input. Please enter a valid index and data format.")


print(edit_transaction)

# delete_a_transaction
def delete_transaction(df):
    delete_transactions = df
    delete_transactions['Date'] = pd.to_datetime(delete_transactions['Date'])
    try:
        # Prompt for the index of the transaction to delete
        index = int(input("Enter the index of the transaction to delete: "))

        # Check if the index is valid
        if index not in delete_transactions.index:
            print("Invalid index.")
            return


        transactions = delete_transactions.drop(index).reset_index(drop=True)

        print("Transaction deleted successfully!")
    except ValueError:
        print("Error: Invalid input. Please enter a valid index.")



print(delete_transaction)


