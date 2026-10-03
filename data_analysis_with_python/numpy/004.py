"""
Q4. — Medium
Create a NumPy array containing the numbers from 1 to 10.
Print:
●​ how many elements it contains
●​ the number of dimensions it has
●​ its shape
Use NumPy's properties/attributes rather than manually counting.
"""

import numpy as np

numbers =  np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(numbers.size) # prints how many elements it contains.
print(numbers.ndim) # prints the number of dimensions it has.
print(numbers.shape) # prints it's shape.