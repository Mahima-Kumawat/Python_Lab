# Write a function in Python to count and display the total number of words in a text file “ABC.txt”


f=open("ABC.txt", "w")
f.write("Hello, My name is Mahima Kumawat.")
f.close()

try:
    with open("ABC.txt", 'r') as file:
        text = file.read()
        words = text.split()
        word_count = len(words)
        print(f"Total number of words in ABC.txt: {word_count}")
except FileNotFoundError:
    print("The file ABC.txt does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


#Output=>

Total number of words in ABC.txt: 6
