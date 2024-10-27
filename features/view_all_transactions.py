import pandas as pd


def view_all_transactions(df: pd.DataFrame):

    if df is None:
        print("A csv file is not imported yet.")
        return

    print("--- All Transactions ---")
    print(df)
    
    return
