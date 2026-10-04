"""
Q12. — Tricky — Find the mistake
A beginner writes:
marks = np.array([45, 60, 75, 90])
result = marks > 50 and marks < 90
print(result)
This gives an error.
Find the mistake, explain why it happens, and correct the condition so that it selects values
between 50 and 90.
"""

import numpy as np

marks = np.array([45, 60, 75, 90])
result = (marks > 50) & (marks < 90)

print(result)

"""
The mistake is using and in numpy arrays.
we don't use 'and' in numpy to get both
conditions but we use '&' in numpy to get both conditions.

We also put parenthesis around each comparison:
(marks > 50) & (marks < 90)
"""