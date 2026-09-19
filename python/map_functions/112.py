"""
Q12. — Tricky
Predict what happens when this code runs:
numbers = [1, 2, 3]
result = map(lambda x: x * 2, numbers)
print(list(result))
print(list(result))
Will both print() statements produce the same transformed numbers?
Explain why or why not.
"""

numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(list(result))
print(list(result))
# we already consumed all of our values in first statement.
# so, in second statement list function tries to again go to the same map object, but the map object iterator has been exhausted.