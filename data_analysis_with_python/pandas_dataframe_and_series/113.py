"""
Q13. — Mixed
Write a function that receives a DataFrame containing a marks column.
The function should find all students who passed.
Assume:
●​ 40 or above = pass
●​ below 40 = fail
Test the function using:
students = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [35, 72, 39, 91]
})
"""

import pandas as pd

students = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [35, 72, 39, 91]
})

def passed_students(students):
    print(students[students['marks'] >= 40])

passed_students(students)