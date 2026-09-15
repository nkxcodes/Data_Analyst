"""
Q7.​
You are making a simple shopping program.
A customer gets free delivery if their purchase amount is ₹500 or more.
Store the purchase amount in a variable and display an appropriate message telling the
customer whether they qualify for free delivery.
"""

purchase_amount = int(input('Enter purchase amount: '))
free_delivery = False

if purchase_amount >= 500:
    free_delivery = True

if free_delivery:
    print('You will get free delivery.')
else:
    print('Sorry! You will not get free delivery.')