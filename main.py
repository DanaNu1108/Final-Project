import pandas as pd

# modules
import modules.data_management as data_management
import modules.file_transfer_management as file_transfer_management
import modules.data_analysis as data_analysis
import modules.data_visualization as data_visualization

# constants
from constants import common_error_type_to_error_message
from constants import AppFeature


def main():
    # Initialize data frame
    current_data_frame: pd.DataFrame = pd.DataFrame()

    while True:
        print("=== Personal Finance Tracker ===")
        
        # Let the user select a csv file if it's not imported yet
        if current_data_frame.empty:
            current_data_frame = file_transfer_management.import_a_csv_file(current_data_frame)
            print("")
            continue
        
        # Display all features
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
                data_management.view_transactions_by_date(current_data_frame)
                print("")

            case AppFeature.ADD_A_TRANSACTION:
                current_data_frame = data_management.add_transaction(current_data_frame)
                print("")
                
            case AppFeature.EDIT_A_TRANSACTION:
                current_data_frame = data_management.edit_transaction(current_data_frame)
                print("")

            case AppFeature.DELETE_A_TRANSACTION:
                current_data_frame = data_management.delete_transaction(current_data_frame)
                print("")

            case AppFeature.ANALYZE_SPENDING_BY_CATEGORY:
                data_analysis.analyze_spending_by_category(current_data_frame)
                print("")

            case AppFeature.CALCULATE_AVERAGE_MONTHLY_SPENDING:
                data_analysis.calculate_average_monthly_spending(current_data_frame)
                print("")
                
            case AppFeature.SHOW_TOP_SPENDING_CATEGORY:
                data_analysis.show_top_spending_category(current_data_frame)
                print("")

            case AppFeature.VISUALIZE_MONTHLY_SPENDING_TREND:
                data_visualization.visualize_monthly_spending_trend(current_data_frame)
                print("")

            case AppFeature.VISUALIZE_SPENDING_BY_CATEGORY:
                data_visualization.visualize_spending_by_category(current_data_frame)
                print("")

            case AppFeature.VISUALIZE_PERCENTAGE_DISTRIBUTION:
                data_visualization.visualize_percentage_distribution(current_data_frame)
                print("")

            case AppFeature.SAVE_TRANSACTIONS_TO_CSV:
                file_transfer_management.save_transactions_to_csv(current_data_frame)
                print("")

            case AppFeature.EXIT:
                print("Exiting the Personal Finance Tracker. Goodbye!")
                print("")
                break


def display_menu():
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
