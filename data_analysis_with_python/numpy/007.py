"""
Q7. — Application
You have the marks of five students:
[72, 85, 64, 91, 78]
Store them in a NumPy array.
Now calculate the average marks and find the highest marks.
Don't manually calculate them using a loop.
"""

import numpy as np

marks = [72, 85, 64, 91, 78]

marks_02 = np.array(marks)

# .mean() method is used to get average in numpy array.
print(marks_02.mean())

# .max() is used to find the highest element in numpy array.
print(marks_02.max())