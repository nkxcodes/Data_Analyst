"""
Q4.​
Create a program that checks whether a number is:
●​ positive
●​ negative
●​ zeroMake sure that exactly the appropriate message is displayed for each case.
"""

number = int(input('Enter a number: '))

if number > 0:
    print('Positive')
elif number < 0:
    print('Negative')
else:
    print('Zero')