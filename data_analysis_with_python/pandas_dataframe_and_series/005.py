"""
Q5. — Medium
Using the same students DataFrame:
Select and print only the name column.
Then select both name and marks columns together.
Observe the difference between selecting one column and multiple columns.
"""

import pandas as pd

students = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [72, 85, 64, 91],
"age": [17, 18, 17, 18]
})

print(students['name'])
print(students[['name', 'marks']])