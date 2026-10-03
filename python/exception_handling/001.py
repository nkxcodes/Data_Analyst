"""
Q1. — Easy
Write a program that asks the user to enter a number and divides 100 by that number.
Use try and except so the program does not crash when the user enters 0.
"""

try:
    number = int(input('Enter a Number: '))
    calculation = 100 / number
except ZeroDivisionError:
    print('Cannot Divide By Zero')
except ValueError:
    print('Entered Value is Wrong!')
else:
    print(f'Result: {calculation}')
finally:
    print('Execution Completed!')