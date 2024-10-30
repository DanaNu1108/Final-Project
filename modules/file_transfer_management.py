import glob
import pandas as pd
from constants import common_error_type_to_error_message

targetDir = "./csv_files"


def import_a_csv_file(df: pd.DataFrame) -> pd.DataFrame:

    # Find all the csv file paths in the "csv_files" directory.
    file_paths = glob.glob(targetDir + "/*.csv")

    # There is no file to import in the directory
    if len(file_paths) == 0:
        print(common_error_type_to_error_message["NO_FILE_EXISTS"])
        # Return inputed Dataframe as it is
        return df

    # Print all file names
    print("Select file number to import.")
    for i in range(len(file_paths)):
        file_path = file_paths[i]
        file_name = file_path[file_path.rfind("/") + 1 :]
        print(f"{i}. {file_name}")

    # Receive a user input and specify the file based on it.
    user_input_number = validated_file_number(file_paths)
    selected_file_path = file_paths[user_input_number]

    # Import the selected file
    try:
        df = pd.read_csv(selected_file_path)
    except Exception as e:
        print("The exception: {}".format(e))
        print(common_error_type_to_error_message["ERROR_OCCURRED"])
        # Replace the dataframe with None in order to encourage the user to import a proper file
        df = None
    else:
        file_name = selected_file_path[selected_file_path.rfind("/") + 1 :]
        print(f"'{file_name}' has been imported successfully.")
    finally:
        return df


def save_transactions_to_csv(df: pd.DataFrame) -> None:

    if df is None:
        print(common_error_type_to_error_message["NO_FILE_IMPORTED"])
        return

    # Receive a user input
    input_file_name = validated_file_name()

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
        
        print("")
        return input_file_name


def validated_file_number(file_paths: list) -> int:
    while True:
        user_input = input("Enter the file number: ")

        if not user_input.isnumeric():
            print(common_error_type_to_error_message["INVALID_NUMBER"])
            continue

        user_input_number = int(user_input)

        if not user_input_number in range(len(file_paths)):
            available_numbers_str = f"0 - {len(file_paths)-1}"  # Ex. "0 - 11"
            print(f"Please enter a number {available_numbers_str}.")
            continue
        
        print("")
        return user_input_number
