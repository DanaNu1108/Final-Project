import pandas as pd
import modules.data_management as data_management
import modules.file_transfer_management as file_transfer_management
from constants import common_error_type_to_error_message
from constants import AppFeature


def main():
    # Initialize data frame
    current_data_frame: pd.DataFrame = None

    while True:
        display_menu()
        user_input = validated_user_input()
        selected_feature = AppFeature.get_by_code(user_input)

        # Call the selected feature function
        match selected_feature:
            case AppFeature.IMPORT_A_CSV_FILE:
                current_data_frame = file_transfer_management.import_a_csv_file(current_data_frame)
                print("")

            case AppFeature.VIEW_ALL_TRANSACTIONS:
                data_management.view_all_transactions(current_data_frame)
                print("")

            case AppFeature.VIEW_TRANSACTIONS_BY_DATE_RANGE:
                print("not implemented yet")

            case AppFeature.ADD_A_TRANSACTION:
                print("not implemented yet")

            case AppFeature.EDIT_A_TRANSACTION:
                print("not implemented yet")

            case AppFeature.DELETE_A_TRANSACTION:
                print("not implemented yet")

            case AppFeature.ANALYZE_SPENDING_BY_CATEGORY:
                print("not implemented yet")

            case AppFeature.CALCULATE_AVERAGE_MONTHLY_SPENDING:
                print("not implemented yet")

            case AppFeature.SHOW_TOP_SPENDING_CATEGORY:
                print("not implemented yet")

            case AppFeature.VISUALIZE_MONTHLY_SPENDING_TREND:
                print("not implemented yet")

            case AppFeature.SAVE_TRANSACTIONS_TO_CSV:
                file_transfer_management.save_transactions_to_csv(current_data_frame)
                print("")

            case AppFeature.EXIT:
                print("Exiting the Personal Finance Tracker. Goodbye!")
                print("")
                break


def display_menu():
    print("=== Personal Finance Tracker ===")

    for feature in AppFeature.members_as_list():
        print(f"{feature.code}. {feature.display_name}")


def validated_user_input():
    feature_list = AppFeature.members_as_list()
    available_options_str = f"{feature_list[0].code} - {feature_list[len(feature_list)-1].code}"  # Ex. "0 - 11"

    while True:
        user_input = input(f"Choose an option ({available_options_str}): ")

        # Empty or null check
        if user_input == "" or user_input is None:
            print(common_error_type_to_error_message["VALUE_IS_EMPTY_OR_NULL"])
            continue

        # Check if the value is defined
        if AppFeature.get_by_code(user_input) is None:
            print(f"Please choose an option {available_options_str}.")
            continue

        print("")
        return user_input


if __name__ == "__main__":
    main()
