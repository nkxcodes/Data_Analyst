"""
Q9.​
Create a program that asks the user for a number and keeps asking for another number until
the user enters 0.
When 0 is entered, stop taking numbers and display the sum of all the numbers entered before
it.
"""

is_running = True

while is_running:
    num = int(input('Enter a number: '))
    if num == 0:
        is_running = False