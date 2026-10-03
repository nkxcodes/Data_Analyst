"""
Q3. — Easy
Create a program that asks the user for two numbers and divides the first number by the
second.
Handle the two possible problems:
●​ The user enters something that isn't a number.
●​ The second number is 0.
"""

try:
    number = int(input('Enter a Number: '))
    divide_by = int(input('Divide By: '))
    calculation = number / divide_by
except ValueError:
    print('Enter valued is not a valid integer!')
except ZeroDivisionError:
    print('Cannot divide by zero!')
else:
    print(f'Result: {calculation}')
finally:
    print('Execution completed!')