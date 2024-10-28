import tkinter as tk
from tkinter import filedialog
import pandas as pd
from constants import common_error_type_to_error_message


def import_a_csv_file(df: pd.DataFrame) -> pd.DataFrame:
    root = tk.Tk()
    root.withdraw()

    fTyp = [("", "*.csv")]
    iDir = "./csv_files"
    file_path = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)

    # No file has been selected(= Cancel button has been pressed)
    if file_path == "":
        print(common_error_type_to_error_message["NO_FILE_SELECTED"])
        # Return inputed Dataframe as it is
        return df

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print("The exception: {}".format(e))
        print(common_error_type_to_error_message["ERROR_OCCURRED"])
        # Replace the dataframe with None in order to encourage the user to import a proper file
        df = None
    else:
        file_name = file_path[file_path.rfind("/") + 1 :]
        print(f"'{file_name}' has been imported successfully.")
    finally:
        return df


def save_transactions_to_csv(df: pd.DataFrame) -> None:

    if df is None:
        print(common_error_type_to_error_message["NO_FILE_IMPORTED"])
        return

    input_file_name = validated_file_name()
    targetDir = "./csv_files"

    try:
        df.to_csv(path_or_buf=targetDir + "/" + input_file_name, index=False)
    except Exception as e:
        print("The exception: {}".format(e))
        print(common_error_type_to_error_message["ERROR_OCCURRED"])
    else:
        print(f"Transactions saved to '{input_file_name}' successfully!")
    finally:
        return


def validated_file_name() -> str:
    while True:
        input_file_name = input("Enter file name to save (e.g., 'transactions.csv'): ")

        # Empty or null check
        if input_file_name == "" or input_file_name is None:
            print(common_error_type_to_error_message["VALUE_IS_EMPTY_OR_NULL"])
            continue

        if input_file_name[-4:] != ".csv":
            print(common_error_type_to_error_message["INVALID_FILE_EXTENSION"])
            continue

        return input_file_name
