"""
Q6. — Medium
Create a program that can encounter different types of errors while processing user input.
Handle these separately:
●​ invalid number input
●​ division by zero
Make sure your program gives a different message for each type of problem.
"""

try:
    number = int(input('Enter a number: '))
    divide_by = int(input('Divide by: '))
    calculation = number / divide_by
except ValueError:
    print('Entered number is not a valid integer!')
except ZeroDivisionError:
    print('Cannot divide by zero!')
except Exception as e:
    print(e)
else:
    print(F'Result: {calculation}')
finally:
    print('Execution completed!')