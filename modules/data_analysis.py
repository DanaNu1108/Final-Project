import pandas as pd
import calendar

file_path = "../csv_files/sampledata.csv"
df = pd.read_csv(file_path)

print(df)

# data sample
#        Date       Category        Description   Amount     Type
# 0   2024-10-01       Food            Grocery    50.75  Expense

# analyze_spending_by_category
# def analyze_spending_by_category():
df_category = df.loc[:, ["Category", "Amount", "Type"]]
type_expense = df_category[df_category["Type"].isin(["Expense"])]
spending_by_category = type_expense.groupby("Category")["Amount"].agg(Total_Spending = 'sum')
spending_by_category.loc['Total']= spending_by_category.sum()
print(spending_by_category)



# calculate_average_monthly_spending
# def calculate_average_monthly_spending():

df_date = df.loc[:, ["Date", "Amount", "Type"]]
df_date["Date"] = pd.to_datetime(df_date["Date"])
df_date["Month"] = df_date["Date"].dt.month.apply(lambda x: calendar.month_abbr[x])
df_date["Year"] = df_date["Date"].dt.year

monthly_spending = df_date.groupby(["Month","Type"])["Amount"].mean()
print(monthly_spending)


# show_top_spending_category
# def show_top_spending_category():
top_spending = spending_by_category.sort_values(by="Total_Spending", ascending=False)
print(top_spending[0:1])