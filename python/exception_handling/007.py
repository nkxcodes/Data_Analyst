"""
Q7. — Application
You are creating a simple calculator.
The user enters:
●​ first number
●​ operator (+, -, *, /)
●​ second number
Make the calculator continue running without crashing if the user:
●​ enters invalid numbers
●​ tries to divide by zero
You don't need to handle every possible programming error—focus on the errors that can
reasonably come from user input.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

try:
    first_number = int(input('Enter first number: '))
    operator = input('Enter Operator(+, -, *, /): ')
    second_number = int(input('Enter second number: '))

    if operator == '+':
        result = add(first_number, second_number)
    elif operator == '-':
        result = subtract(first_number, second_number)
    elif operator == '*':
        result = multiply(first_number, second_number)
    elif operator == '/':
        result = divide(first_number, second_number)
except ValueError:
    print('Entered value is not valid!')
except ZeroDivisionError:
    print('Cannot divide by zero!')
else:
    print(f'Result: {result}')
finally:
    print('Execution completed!')