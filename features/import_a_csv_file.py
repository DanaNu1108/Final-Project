import tkinter as tk
from tkinter import filedialog
import pandas as pd


def import_file():
    root = tk.Tk()
    root.withdraw()

    fTyp = [("", "*.csv")]
    iDir = "./"
    file_path = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print("The exception: {}".format(e))
        print("An error occured. Please try again.")
        df = None
    else:
        print("A csv file is imported successfully.")
    finally:
        return df
