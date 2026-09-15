"""
Q9.​
A cinema has different ticket prices based on age:
●​
●​
●​
●​
below 5 → Free
5–17 → Child ticket
18–59 → Adult ticket
60 or above → Senior ticket
Store the person's age in a variable and determine which ticket category they belong to.
"""

age = int(input('Enter age: '))
ticket_category = ''

if age >= 60:
    ticket_category = 'Senior ticket'
elif age >= 18:
    ticket_category = 'Adult ticket'
elif age >= 5:
    ticket_category = ' Child ticket'
elif age < 5:
    ticket_category = 'Free'

print(f'Ticket category: {ticket_category}')