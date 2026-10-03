"""
Q2. — Easy
Ask the user to enter an integer.
If the user enters something that isn't a valid integer, handle the error gracefully instead of
allowing the program to crash.
"""

try:
    number = int(input('Enter a Integer: '))
except ValueError:
    print('Entered value is not a valid integer!')
else:
    print(number)
finally:
    print('Execution completed!')