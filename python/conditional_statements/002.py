"""
Q2.​
Create a variable called number.
Check whether the number is positive. If it is positive, print:
Positive number
Test your program with both a positive and a negative number.
"""

number = int(input('Enter a number: '))

if number > 0:
    print('Positive number')
elif number < 0:
    print('Negative')