"""
Q2. — Easy
Create a file called notes.txt containing three lines:
Python
Pandas
Linux
Read the entire file and print its contents.
"""

with open('notes.txt', 'w') as file:
    file.write('Python\n')
    file.write('Pandas\n')
    file.write('Linux')

with open('notes.txt', 'r') as file:
    print(file.read())