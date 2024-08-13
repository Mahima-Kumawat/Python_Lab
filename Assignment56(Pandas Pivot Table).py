# Write a Pandas program to create a Pivot table and find the item wise unit sold.

import pandas as pd

# Read the CSV file
df = pd.read_csv('C:/Users/91702/Downloads/salesdata.csv')

# Create a Pivot Table to find the total units sold for each item
pivot_table = pd.pivot_table(df, 
                             values='Units',  # The column you want to aggregate
                             index='Item',  # The column to group by
                             aggfunc='sum')  # The aggregation function to use (sum in this case)

# Display the Pivot Table
print(pivot_table)


# Output=>

              Units
Item               
Cell Phone      278
Desk             10
Home Theater    722
Television      716
Video Games     395






