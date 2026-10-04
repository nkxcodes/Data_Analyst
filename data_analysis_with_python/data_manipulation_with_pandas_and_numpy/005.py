"""
Q5. — Medium
Given:
df = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [75, 88, 92, 65]
})
Calculate:
●​ total marks
●​ average marks
●​ highest marks
●​ lowest marks
Use Pandas aggregation rather than manually calculating the values.
"""

import pandas as pd

df = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [75, 88, 92, 65]
})

total_marks = df['marks'].sum()
average_marks = df['marks'].mean()
highest_marks = df['marks'].max()
lowest_marks = df['marks'].min()

print(total_marks)
print(average_marks)
print(highest_marks)
print(lowest_marks)