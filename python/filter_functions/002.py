"""
Q2. — Easy
You have:
numbers = [5, 12, 7, 20, 3, 15]
Use filter() to keep only the numbers greater than 10.
"""

numbers = [5, 12, 7, 20, 3, 15]

result = filter(lambda x: x > 10, numbers)

print(list(result))