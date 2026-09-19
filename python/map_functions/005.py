"""
Q5. — Medium
Rewrite the previous type of problem using a lambda function directly inside map().
Use:
[3, 5, 7, 9]
and create a result containing their cubes.
"""

numbers = [3, 5, 7, 9]

result = map(lambda x: x * x * x, numbers)

print(list(result))