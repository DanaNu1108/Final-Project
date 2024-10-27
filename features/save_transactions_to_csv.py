import pandas as pd
from constants import common_error_type_to_error_message


def save_to_csv(df: pd.DataFrame) -> None:

    if df is None:
        print(common_error_type_to_error_message["NO_FILE_IMPORTED"])
        return

    input_file_name = validated_file_name()
    targetDir = "./csv_files"

    try:
        df.to_csv(targetDir + "/" + input_file_name)
    except Exception as e:
        print("The exception: {}".format(e))
        print(common_error_type_to_error_message["ERROR_OCCURRED"])
    else:
        print(f"Transactions saved to {input_file_name} successfully!")
    finally:
        return


def validated_file_name() -> str:
    while True:
        input_file_name = input("Enter file name to save (e.g., 'transactions.csv'): ")
        print(input_file_name[-4:])
        # Empty or null check
        if input_file_name == "" or input_file_name is None:
            print(common_error_type_to_error_message["VALUE_IS_EMPTY_OR_NULL"])
            continue

        if input_file_name[-4:] != ".csv":
            print(common_error_type_to_error_message["INVALID_FILE_EXTENSION"])
            continue

        return input_file_name
