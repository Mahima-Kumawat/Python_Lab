#Write a Python program to get the key, value and item in a dictionary.


# Input dictionary
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Print header
print("key\tvalue")
print("-" * 15)

# Iterate over dictionary items and print key-value pairs
for key, value in dict_num.items():
    print(f"{key}\t{value}")


#Output=>

key	value
---------------
1	10
2	20
3	30
4	40
5	50
6	60
