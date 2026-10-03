"""
Q5. — Medium
Write a program that asks the user for the name of a file and attempts to open and read it.
Handle the situation where the requested file does not exist.
Also think about why catching a specific exception is better than simply catching every possible
exception.
"""

try:
    u_file = input('Enter file name: ')
    with open(u_file, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('Given file does not exist!')
else:
    print(content)
finally:
    print('Execution completed!')