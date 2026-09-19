"""
Q10. — Tricky
Predict what type of thing result is without running the code:
numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(result)
Will print(result) directly display:
●​ the transformed numbers,
●​ a list,
●​ or something else?
Then explain why.
"""

numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(result) # result is a map object, not a list.