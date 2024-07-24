# Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 


import numpy as np

# Daily temperature readings for a city
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

# Identify hot days (temperature > 35 degrees Celsius)
hot_day_indices = np.where(temperatures > 35)

# Identify cold days (temperature < 5 degrees Celsius)
cold_day_indices = np.where(temperatures < 5)

# Print the results
print("Hot Days:")
print("Day\tTemperature")
for index in hot_day_indices[0]:
    print(f"{index+1}\t{temperatures[index]:.1f}")
    
print("\nCold Days:")
print("Day\tTemperature")
for index in cold_day_indices[0]:
    print(f"{index+1}\t{temperatures[index]:.1f}")


#Output=>

Hot Days:
Day	Temperature
3	36.8
6	38.7
10	37.2

Cold Days:
Day	Temperature
11	4.0
14	-4.0
15	-12.0





