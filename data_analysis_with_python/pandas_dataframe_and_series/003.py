"""
Q3. — Easy
Given:
marks = pd.Series([72, 85, 64, 91, 78])
Find and print:
●​ the first value
●​ the third value
●​ the last value
Use indexing.
"""

import pandas as pd

marks = pd.Series([72, 85, 64, 91, 78])

print(marks[0]) # Prints first element
print(marks[2])  # Prints third element
print(marks.iloc[-1]) # Prints last element