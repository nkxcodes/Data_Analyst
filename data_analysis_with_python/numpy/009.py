"""
Q9. — Application
Given:
marks = np.array([45, 67, 82, 39, 91, 55, 76])
You want to know which students scored more than 60.
Create a condition that compares the array with 60 and print the result.
Then use that result to obtain only the marks above 60.
"""

import numpy as np

marks = np.array([45, 67, 82, 39, 91, 55, 76])

more_than_60 = marks > 60
above_60 = marks[more_than_60]

print(above_60)