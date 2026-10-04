"""
Q10. — Tricky
Predict what each of these will produce before running them:
arr = np.array([10, 20, 30, 40])
print(arr > 20)
print(arr == 20)
print(arr < 100)
Then run the code.
Explain why the result is an array of True/False values rather than one True/False value.
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr > 20)
print(arr == 20)
print(arr < 100)

"""
result is an array of True/False values
rather than one True/False values because NumPy
compares every element separately.
"""