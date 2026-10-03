"""
Q2. — Easy
Create a NumPy array from this Python list:
[5, 10, 15, 20, 25]
Then print its type.
What is different about the NumPy array compared with the original Python list?
"""

import numpy as np

numbers = np.array([5, 10, 15, 20, 25])

print(type(numbers))

"""
Python list - general purpose collection of values.
NumPy array - designed especially for fast numerical
calculations and can perform operations on many values 
efficiently.
"""