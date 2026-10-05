"""
Q12. — Tricky — Understand merging
what the merged result should contain:
students = pd.DataFrame({
"id": [1, 2, 3],
"name": ["Aman", "Priya", "Rahul"]
})
marks = pd.DataFrame({
"id": [1, 2, 4],
"marks": [75, 88, 91]
})
Merge these DataFrames using id as the key.
Pay special attention to:
●​ Which students have matching records?
●​ What happens to student 3?
●​ What happens to id = 4?
●​ Why does choosing the type of merge matter?
"""

import pandas as pd

students = pd.DataFrame({
"id": [1, 2, 3],
"name": ["Aman", "Priya", "Rahul"]
})
marks = pd.DataFrame({
"id": [1, 2, 4],
"marks": [75, 88, 91]
})

merged_tables = pd.merge(students, marks, on='id', how='inner')

print(merged_tables)

"""
1 -Aman and Priya has matching records.
2 - Student 3 will not get display because we use inner
join, in it only matching values will be given
3 - id  = 4 also will not get display because there is
no matching values.
4 - Choosing the type of merge matter because
it determines the result.
"""