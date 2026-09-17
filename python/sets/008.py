"""
Q8.​
You receive a list of numbers containing many duplicates.
For example:
[10, 20, 10, 30, 40, 20, 50, 30]
Create a new collection containing only the unique numbers.
The original list should remain unchanged.
"""

numbers = [10, 20, 10, 30, 40, 20, 50, 30]

unique_numbers = set(numbers)

print(numbers)
print(unique_numbers)