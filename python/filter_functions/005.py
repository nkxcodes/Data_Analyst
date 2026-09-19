"""
Q5. — Medium
Solve a filtering problem using a lambda function directly inside filter().
Given:
numbers = [3, 8, 11, 14, 17, 20, 25]
Keep only the numbers that are divisible by 2.
"""


numbers = [3, 8, 11, 14, 17, 20, 25]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))