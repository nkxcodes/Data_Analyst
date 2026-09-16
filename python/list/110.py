"""
Q10.​
Predict what the following program will print before running it:
numbers = [10, 20, 30]
other = numbers
other[0] = 100
print(numbers)
print(other)
Then run it.
Explain why changing other also appears to change numbers.
"""

numbers = [10, 20, 30]

other = numbers
other[0] =  100

print(numbers)
print(other)

"""
Changes appeared in both list because other = numbers
does not create a new list, both variables is pointing to
the same list.

so, any changes will appear in both variables
"""