"""
Q5. — Medium
Given:
arr = np.array([10, 20, 30, 40, 50, 60])
Create and print:
1.​ The first three elements
2.​ The last three elements
3.​ Every second element
Use slicing.
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[0:3])
print(arr[-3:])
print(arr[0::2])