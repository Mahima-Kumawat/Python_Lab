# Write a Pandas program to create a Pivot table and find the total sale amount region wise, manager wise, sales man wise.


import pandas as pd

# Read the CSV file
df = pd.read_csv('C:/Users/91702/Downloads/salesdata.csv')

# Create a Pivot Table
pivot_table = pd.pivot_table(df, 
                             values='Sale_amt',  # The column you want to aggregate
                             index=['Region', 'Manager', 'SalesMan'],  # The columns you want to group by
                             aggfunc='sum')  # The aggregation function to use (sum in this case)

# Display the Pivot Table
print(pivot_table)


# Output=>

                           Sale_amt
Region  Manager SalesMan           
Central Douglas John       124016.0
        Hermann Luis       206373.0
                Shelli      33698.0
                Sigal      125037.5
        Marth   Steven      14000.0
        Martha  Steven     185690.0
        Timothy David      140955.0
East    Douglas Karen       48204.0
        Martha  Alexander  236703.0
                Diana       36100.0
West    Douglas Michael     66836.0
        Timothy Stephen     88063.0





