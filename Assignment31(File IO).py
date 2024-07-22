# Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.


f=open("ABC.txt", "w")
f.write("Hello, My name is Mahima Kumawat.")
f.close()

try:
    with open("ABC.txt", 'r') as file:
        for line in file:
            print(line, end='')
except FileNotFoundError:
    print("The file ABC.txt does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


#Output=>

#Hello, My name is Mahima Kumawat.
