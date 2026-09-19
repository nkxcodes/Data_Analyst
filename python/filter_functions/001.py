"""
Q1. — Easy
You have:
numbers = [1, 2, 3, 4, 5, 6]
Use filter() to keep only the even numbers.
"""

numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))