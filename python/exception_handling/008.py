"""
Q8. — Application
A program needs to read a file containing numbers, one number per line.
Some lines may contain invalid data such as:
25
40
hello
60
abc
80
Read the file and process the valid numbers while preventing an invalid line from stopping the
entire program.
Think about where the try/except should be placed.
"""

with open('numbers.txt', 'r') as file:
    content = file.read()
    content = content.split()

    for line in content:
        try:
            number = int(line)
        except ValueError:
            print('Invalid number!')
        else:
            print(number)