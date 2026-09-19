"""
Q13. — Mixed
You have:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Create a result containing numbers that are:
●​ even
●​ and greater than 5
Use filter() together with a condition.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = filter(lambda x: x % 2 == 0 and x > 5, numbers)

print(list(result))