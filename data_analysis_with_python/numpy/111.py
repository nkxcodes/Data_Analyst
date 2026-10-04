"""
Q11. — Tricky
You want to select marks that satisfy both conditions:
●​ greater than or equal to 50
●​ less than or equal to 80
Given:
marks = np.array([35, 50, 62, 79, 80, 85, 95])
Create the logical condition and use it to select the matching marks.
Also think about why normal Python and is not the appropriate operator for comparing the
whole NumPy array this way.
"""

import numpy as np

marks = np.array([35, 50, 62, 79, 80, 85, 95])

print(marks[(marks >= 50) & (marks <= 80)])