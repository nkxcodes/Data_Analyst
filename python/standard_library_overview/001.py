"""
Q1. — Easy
Import Python's array module.
Create an integer array containing:
10, 20, 30, 40, 50
Then:
1.​ Print the array.
2.​ Access the third element.
3.​ Add one more number to the array.
"""

from array import array

numbers = array('i', [10, 20, 30, 40, 50])

print(numbers[2])

numbers.append(60)

print(list(numbers))