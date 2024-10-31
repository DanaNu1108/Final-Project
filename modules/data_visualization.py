import matplotlib.pyplot as plt
import pandas as pd
import calendar
import numpy as np



# Monthly Spending Trend: Visualize spending trends over time using a line chart.
def visualize_monthly_spending_trend(df: pd.DataFrame):

    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values(by="Date", ascending=True)
    df = df.reset_index(drop=True)

    df_date = df.loc[:, ["Date", "Amount", "Type"]]
    df_date["Month"] = df_date["Date"].dt.month.apply(lambda x: calendar.month_abbr[x])
    df_date["Year"] = df_date["Date"].dt.year



    df_date_new_arrange = df_date.pivot_table(index=['Year', 'Month'], columns='Type',
                             values='Amount', aggfunc='sum', sort=False)

    df_date_new_arrange.plot(kind='line', color=['red','green'])
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.title("Monthly Spending Trend", fontsize=14, fontweight='bold')
    plt.legend()

    plt.show()


# Spending by Category: Create a bar chart showing total spending by category.
def visualize_spending_by_category(df: pd.DataFrame):

    df_expense = df.loc[df["Type"] == "Expense"]
    df_category = df_expense.groupby("Category")["Amount"].agg(Amount='sum').reset_index()
    df_category = df_category.sort_values(by='Amount', ascending=False)
    df_category = df_category.set_index("Category")

    df_category.plot(kind='bar', color='teal')
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title("Spending by Category", fontsize=14, fontweight='bold')

    plt.show()

# Percentage Distribution: Generate a pie chart representing the distribution of spending across categories.
def visualize_percentage_distribution(df: pd.DataFrame):

    df_expense = df.loc[df["Type"] == "Expense"]
    df_category = df_expense.groupby("Category")["Amount"].agg(Amount='sum').reset_index()
    df_category = df_category.sort_values(by='Amount', ascending=False)

    labels = df_category["Category"]
    data = df_category["Amount"]

    cmap = plt.get_cmap('summer')
    colors = cmap(np.linspace(0, 1, len(data)))

    plt.pie(data, labels=labels, autopct='%1.1f%%', colors=colors)
    plt.title("Spending % per Category", fontsize=14, fontweight='bold')

    plt.show()
