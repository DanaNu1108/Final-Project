import constants as cnst
import pandas as pd
import features.import_a_csv_file as import_a_csv_file


def main():
    df: pd.DataFrame = None

    while True:
        display_menu()
        user_input = validated_user_input()

        # Call the selected feature function
        match user_input:
            case "0":
                df = import_a_csv_file.import_file()
                print("")

            case "1":
                print("not implemented yet")

            case "2":
                print("not implemented yet")

            case "3":
                print("not implemented yet")

            case "4":
                print("not implemented yet")

            case "5":
                print("not implemented yet")

            case "6":
                print("not implemented yet")

            case "7":
                print("not implemented yet")

            case "8":
                print("not implemented yet")

            case "9":
                print("not implemented yet")

            case "10":
                print("not implemented yet")

            case "11":
                print("Exiting the Personal Finance Tracker. Goodbye!")
                break

            case _:
                print("not implemented yet")


def display_menu():
    print("=== Personal Finance Tracker ===")

    for k, v in cnst.index_to_display_menu_name.items():
        print(f"{k}. {v}")


def validated_user_input():
    while True:
        user_input = input("Choose an option (1-11): ")

        # Empty or null check
        if user_input == "" or user_input is None:
            print(cnst.common_error_type_to_error_message["EMPTY_OR_NULL_ERROR"])
            continue

        # Check if the value is defined
        if not user_input in cnst.index_to_display_menu_name.keys():
            print("Please choose an option 1 - 11.")
            continue

        return user_input


if __name__ == "__main__":
    main()
