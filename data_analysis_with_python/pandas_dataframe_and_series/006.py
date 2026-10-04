"""
Q6. — Medium
Given:
students = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [72, 85, 64, 91],
"age": [17, 18, 17, 18]
})
Select:
1.​ The first row
2.​ The third row
3.​ The first two rows
Try to understand the difference between selecting rows and selecting columns.
"""

import pandas as pd

students = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [72, 85, 64, 91],
"age": [17, 18, 17, 18]
})

# .loc is used to select rows and .iloc is used to select columns.

print(students.loc[0])
print(students.loc[2])
print(students.iloc[0:2])