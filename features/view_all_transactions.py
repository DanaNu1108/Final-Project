import pandas as pd
from constants import common_error_type_to_error_message


def view_all_transactions(df: pd.DataFrame) -> None:

    if df is None:
        print(common_error_type_to_error_message["NO_FILE_IMPORTED"])
        return

    print("--- All Transactions ---")
    print(df)

    return
