"""
Q14.​
Create a program that takes a number from the user.
Determine whether the number is:
●​ even or odd
●​ and whether it is positive, negative, or zero
Your program should give the appropriate result for the number entered.
"""

number = int(input('Enter number: '))
even = False
number_is = ''

if number % 2 == 0:
    even = True

if number > 0:
    number_is = 'Positive'
elif number < 0:
    number_is = 'Negative'
else:
    number_is = 'Zero'

if even:
    print(f'Number is even and {number_is}')
else:
    print(f'Number is odd and {number_is}')