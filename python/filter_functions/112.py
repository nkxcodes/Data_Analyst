"""
Q12. — Tricky
Predict the output before running the code:
numbers = [1, 2, 3, 4, 5]
result = filter(lambda x: x > 2, numbers)
print(list(result))
print(list(result))
Will both print() statements show the same filtered values?
Explain why.
"""

numbers = [1, 2, 3, 4, 5]

result = filter(lambda x: x > 2, numbers)

print(list(result))
print(list(result)) # filter object iterator has been exhausted after first print statement.