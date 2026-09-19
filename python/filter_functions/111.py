"""
Q11. — Tricky
A beginner writes:
numbers = [1, 2, 3, 4, 5]
result = filter(lambda x: x * 2, numbers)
print(list(result))
They expected only the numbers whose double is even.
Find the conceptual mistake in their thinking.
What is filter() actually looking at when deciding whether to keep an item?
"""

numbers = [1, 2, 3, 4, 5]

result = filter(lambda x: (x * 2) % 2 == 0, numbers)

print(list(result))