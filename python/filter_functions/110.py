"""
Q10. — Tricky
Predict what this produces:
numbers = [0, 1, 2, 0, 3, 0, 4]
result = filter(None, numbers)
print(list(result))
Why does filter() behave this way when the first argument is None?
"""

numbers = [0, 1, 2, 0, 3, 0, 4]

result = filter(None, numbers)

print(list(result))

# When we give filter function a None function in it, it just checks for truthy values and keep it.