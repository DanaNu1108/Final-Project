import tkinter as tk
from tkinter import filedialog
import pandas as pd
from constants import common_error_type_to_error_message


def import_file(df: pd.DataFrame) -> pd.DataFrame:
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
