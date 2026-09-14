"""
Q13.​
Create a program that receives a number from the user and stores it in a variable.
Then determine whether the number is:
●​ positive
●​ negative
●​ or zero
Use variables together with a conditional statement.
"""

number = int(input('Enter a number: '))

number_is = ''

if number > 0:
    number_is = 'Positive'
elif number < 0:
    number_is = 'Negative'
else:
    number_is = 'Zero'

print(number_is)