"""
Q2. — Easy
You have:
numbers = [2, 4, 6, 8]
Use map() to create a result containing the square of every number.
"""

numbers = [2, 4, 6, 8]

result = map(lambda x: x ** 2, numbers)

print(list(result))