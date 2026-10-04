"""
Q3. — Easy
Given:
df = pd.DataFrame({
"student_name": ["Aman", "Priya", "Rahul"],
"student_marks": [75, 88, 92],
"student_age": [17, 18, 17]
})
Rename the columns so they become:
name
marks
age
Print the DataFrame.
"""

import pandas as pd

df = pd.DataFrame({
"student_name": ["Aman", "Priya", "Rahul"],
"student_marks": [75, 88, 92],
"student_age": [17, 18, 17]
})

df = df.rename(columns={'student_name':'name', 'student_marks':'marks', 'student_age':'age'})
print(df)