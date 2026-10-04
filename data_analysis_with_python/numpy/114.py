"""
Q14. — Mixed
Write a function called check_marks(marks) that accepts a NumPy array of marks.
The function should:
●​ find students who scored at least 40
●​ find students who scored below 40
●​ print both groups
Test your function with:
np.array([35, 72, 48, 29, 91, 64])
Think about how conditions and logical operators can work together with a NumPy array.
"""

import numpy as np

def check_marks(marks):
    print(marks[marks >= 40])
    print(marks[marks < 40])

arr = np.array([35, 72, 48, 29, 91, 64])

check_marks(arr)