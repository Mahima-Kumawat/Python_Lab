# Create a bar chart to represent monthly expenses in different spending categories and give your conclusion. 


import matplotlib.pyplot as plt

# Data
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, expenses)

# Add title and labels
plt.title('Monthly Expenses by Category')
plt.xlabel('Categories')
plt.ylabel('Expenses (in dollars)')

# Show the chart
plt.show()





