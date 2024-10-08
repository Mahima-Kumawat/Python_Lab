# Suppose you want to track and analyze your household expenses for a month. You have recorded the expenses for various categories, such as groceries, utilities, rent, transportation, and entertainment. You can represent this expense data using a Pandas Series. 


import pandas as pd

# Input data
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]

# Create a Pandas Series
expenses_series = pd.Series(data=expenses, index=categories, name="Monthly Expenses (USD)")

# Display the Series
print(expenses_series)


# Output=>

Groceries          500
Utilities          200
Rent              1200
Transportation     300
Entertainment      150
Name: Monthly Expenses (USD), dtype: int64




