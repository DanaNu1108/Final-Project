from enum import Enum

# Define common error messages
common_error_type_to_error_message = {
    "VALUE_IS_EMPTY_OR_NULL": "Empty or Null value is not acceptable. Please try again.",
    "NO_FILE_IMPORTED": "No csv file is imported yet.",
    "INVALID_FILE_EXTENSION": "The file extension is not .csv.",
    "ERROR_OCCURRED": "An error has occured. Please try again.",
    "NO_FILE_EXISTS": "There is no file to import in the directory.",
    "INVALID_NUMBER": "It's not a valid number. Please try again.",
}


# Define each feature code and display name
class AppFeature(Enum):
    IMPORT_A_CSV_FILE = ("0", "Import a CSV File")
    VIEW_ALL_TRANSACTIONS = ("1", "View All Transactions")
    VIEW_TRANSACTIONS_BY_DATE_RANGE = ("2", "View Transactions by Date Range")
    ADD_A_TRANSACTION = ("3", "Add a Transaction")
    EDIT_A_TRANSACTION = ("4", "Edit a Transaction")
    DELETE_A_TRANSACTION = ("5", "Delete a Transaction")
    ANALYZE_SPENDING_BY_CATEGORY = ("6", "Analyze Spending by Category")
    CALCULATE_AVERAGE_MONTHLY_SPENDING = ("7", "Calculate Average Monthly Spending")
    SHOW_TOP_SPENDING_CATEGORY = ("8", "Show Top Spending Category")
    VISUALIZE_MONTHLY_SPENDING_TREND = ("9", "Visualize Monthly Spending Trend")
    VISUALIZE_SPENDING_BY_CATEGORY = ("10", "Visualize Spending By Category")
    VISUALIZE_PERCENTAGE_DISTRIBUTION = ("11", "Visualize Percentage Distribution")
    SAVE_TRANSACTIONS_TO_CSV = ("12", "Save Transactions to CSV")
    EXIT = ("13", "Exit")

    def __init__(self, code, display_name):
        self.code = code
        self.display_name = display_name

    @classmethod
    def members_as_list(cls):
        return [*cls.__members__.values()]

    @classmethod
    def get_by_code(cls, code):
        for feature in cls.members_as_list():
            if code == feature.code:
                return feature
        # default
        return None
