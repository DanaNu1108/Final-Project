import pandas as pd
import calendar
from tabulate import tabulate
from constants import common_error_type_to_error_message


# analyze_spending_by_category
def analyze_spending_by_category(df:pd.DataFrame):
    
    df_category = df.loc[:, ["Category", "Amount", "Type"]]
    type_expense = df_category[df_category["Type"].isin(["Expense"])]
    spending_by_category = type_expense.groupby("Category")["Amount"].agg(Total_Spending = 'sum')
    spending_by_category.loc['Total']= spending_by_category.sum()

    # ANSI escape code \033[<color>m
    header_color = "\033[33m" # Orange
    reset = "\033[0m"  # Reset to default

    print("\033[36m -> SPENDING BY CATEGORY  \033[0m")
    print(tabulate(spending_by_category, headers=[header_color + 'Category' + reset, header_color + 'Total Spending' + reset], tablefmt='pipe'))



# calculate_average_monthly_spending
def calculate_average_monthly_spending(df:pd.DataFrame):

    df_date = df.loc[:, ["Date", "Amount", "Type"]]
    df_date["Date"] = pd.to_datetime(df_date["Date"])
    df_date["Month"] = df_date["Date"].dt.month.apply(lambda x: calendar.month_abbr[x])
    df_date["Year"] = df_date["Date"].dt.year

    df_date_new_arrange = df_date.pivot_table(index=['Year', 'Month'], columns='Type',
                         values='Amount', aggfunc='mean')

    print("\033[36m -> AVERAGE MONTHLY SPENDING  \033[0m")
    print(tabulate(df_date_new_arrange, headers=['Month', 'Expense', 'Income'], tablefmt='pipe'))



# show_top_spending_category
def show_top_spending_category(df:pd.DataFrame):
    
    top_spending = df.groupby(["Category","Type"])["Amount"].sum().reset_index()
    top_spending = top_spending[top_spending.Type != "Income"]
    top_spending = top_spending.sort_values(by="Amount", ascending=False).set_index("Category")
    top_spending = top_spending.loc[:, ["Amount"]]

    print("\033[36m - TOP SPENDING CATEGORY - \033[0m")
    print(tabulate(top_spending[0:1], headers= ['Category', 'Amount'], tablefmt='pipe'))

