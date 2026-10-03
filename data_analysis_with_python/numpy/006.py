"""
Q6. — Medium
Given:
arr = np.array([10, 20, 30, 40, 50])
Perform these operations:
1.​ Add 5 to every element.
2.​ Multiply every element by 2.
3.​ Subtract 10 from every element.
Observe what happens compared with doing similar operations on a normal Python list.
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr + 5)
print(arr * 2)
print(arr - 10)