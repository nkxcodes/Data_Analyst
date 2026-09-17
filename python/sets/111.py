"""
Q11.​
Find and fix the mistake in this program:
numbers = {}
numbers.add(10)
numbers.add(20)
print(numbers)
The programmer wants numbers to be an empty set and then add values to it.
After fixing it, explain why the original {} does not create an empty set.
"""

numbers = set()

numbers.add(10)
numbers.add(20)

print(numbers)

# because empty {}, python take it as dictionaries not sets
# to create an empty set we have to do set()
# but set with containing values will be a set but empty set will be taken as dictionaries by python.