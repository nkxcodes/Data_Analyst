"""
Q4. — Medium
Given:
students = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [72, 85, 64, 91],
"age": [17, 18, 17, 18]
})
Find out:​
the number of rows
the number of columns
the column names
the data types of the columns
Use Pandas properties rather than manually counting.
"""

import pandas as pd

students = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [72, 85, 64, 91],
"age": [17, 18, 17, 18]
})

print(students.shape[0]) # Prints number of rows
print(students.shape[1]) # Prints number of columns
print(students.columns) # Print the column names
print(students.dtypes) # Print the data types of the columns