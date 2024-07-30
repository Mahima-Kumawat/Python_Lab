# Visualize the daily temperature changes over time in a city and give your conclusion.


import matplotlib.pyplot as plt

# Data
days = list(range(1, 32))
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Create line chart
plt.figure(figsize=(12, 6))
plt.plot(days, temperature, marker='o', color='blue')

# Add title and labels
plt.title('Daily Temperature Changes Over Time')
plt.xlabel('Days')
plt.ylabel('Temperature (°F)')

# Show the chart
plt.grid(True)
plt.show()





