#Write a Python script to concatenate the following dictionaries to create a new one.


# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Initialize an empty dictionary
combined_dict = {}

# Concatenate dictionaries
combined_dict.update(dic1)
combined_dict.update(dic2)
combined_dict.update(dic3)

# Print the combined dictionary
print("Combined Dictionary:", combined_dict)



#Output=>

#Combined Dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
