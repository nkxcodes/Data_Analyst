"""
Q13. — Mixed
You have:
numbers = [1, 2, 3, 4, 5, 6]
Use map() together with a condition so that:
●​ even numbers become "Even"
●​ odd numbers become "Odd"
Your result should contain one "Even" or "Odd" value for every number.
"""

numbers = [1, 2, 3, 4, 5, 6]

result = map(lambda x: 'Even' if x % 2 == 0 else 'Odd', numbers)

print(list(result))