"""
Q14. — Mixed
You have a file called marks.txt containing student marks, one per line.
Some lines may be invalid:
78
91
hello
65
abc
88
Create a program that:
1.​ Reads the file.
2.​ Attempts to convert each line into an integer.
3.​ Ignores invalid lines without stopping the program.
4.​ Calculates the average of the valid marks.
5.​ Uses else and/or finally where they naturally make sense.
Think carefully about what operation should be inside the try block.
"""


with open('marks.txt', 'r') as file:
    content = file.read()
    content = content.split()

    numbers = []
    total = 0

    for line in content:
        try:
            number = int(line)
        except ValueError:
            continue
        else:
            numbers.append(number)
            total += number

    average = total / len(numbers)
