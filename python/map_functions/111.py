"""
Q11. — Tricky
A beginner writes:
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)
print(result[0])
Find the mistake.
Explain why the beginner might expect this to work and what concept about map() they have
misunderstood.
"""

numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, numbers)

print(result[0]) # map returns map object, not a list.
# the beginner has misunderstood that map() list-like object.