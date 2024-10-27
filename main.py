import constants as cnst
import pandas as pd
import features.import_a_csv_file as import_a_csv_file
import features.view_all_transactions as view_all_transactions
from App_Feature import App_Feature


def main():
    # Initialize data frame
    current_data_frame: pd.DataFrame = None
    print(App_Feature.get_by_code("1"))

    while True:
        display_menu()
        user_input = validated_user_input()
        selected_feature = App_Feature.get_by_code(user_input)

        # Call the selected feature function
        match selected_feature:
            case App_Feature.IMPORT_A_CSV_FILE:
                current_data_frame = import_a_csv_file.import_file()
                print("")

            case App_Feature.VIEW_ALL_TRANSACTIONS:
                view_all_transactions.view_all_transactions(current_data_frame)
                print("")

            case App_Feature.VIEW_TRANSACTIONS_BY_DATE_RANGE:
                print("not implemented yet")

            case App_Feature.ADD_A_TRANSACTION:
                print("not implemented yet")

            case App_Feature.EDIT_A_TRANSACTION:
                print("not implemented yet")

            case App_Feature.DELETE_A_TRANSACTION:
                print("not implemented yet")

            case App_Feature.ANALYZE_SPENDING_BY_CATEGORY:
                print("not implemented yet")

            case App_Feature.CALCULATE_AVERAGE_MONTHLY_SPENDING:
                print("not implemented yet")

            case App_Feature.SHOW_TOP_SPENDING_CATEGORY:
                print("not implemented yet")

            case App_Feature.VISUALIZE_MONTHLY_SPENDING_TREND:
                print("not implemented yet")

            case App_Feature.SAVE_TRANSACTIONS_TO_CSV:
                print("not implemented yet")

            case App_Feature.EXIT:
                print("Exiting the Personal Finance Tracker. Goodbye!")
                break

            case _:
                print("not implemented yet")


def display_menu():
    print("=== Personal Finance Tracker ===")

    for feature in App_Feature.members_as_list():
        print(f"{feature.code}. {feature.display_name}")


def validated_user_input():
    feature_list = App_Feature.members_as_list()
    available_options_str = f"{feature_list[0].code} - {feature_list[len(feature_list)-1].code}"  # Ex. "0 - 11"

    while True:
        user_input = input(f"Choose an option ({available_options_str}): ")

        # Empty or null check
        if user_input == "" or user_input is None:
            print(cnst.common_error_type_to_error_message["EMPTY_OR_NULL_ERROR"])
            continue

        # Check if the value is defined
        if App_Feature.get_by_code(user_input) is None:
            print(f"Please choose an option {available_options_str}.")
            continue
        
        print("")
        return user_input


if __name__ == "__main__":
    main()
