"""
Q13. — Mixed
You are given:
numbers = np.array([10, 15, 20, 25, 30, 35, 40])
Using NumPy and a condition, select all numbers that are:
●​ greater than 15
●​ and even
Print the resulting array.
Try to do this without writing a for loop.
"""

import numpy as np

numbers = np.array([10, 15, 20, 25, 30, 35, 40])

conditions = (numbers > 15) & (numbers % 2 == 0)

print(numbers[conditions])