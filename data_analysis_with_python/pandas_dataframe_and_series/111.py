"""
Q11. — Tricky
Given:
students = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul"],
"marks": [75, 85, 65]
})
A beginner writes:
print(students["age"])
The program produces an error.
Find the mistake.
Explain why Pandas cannot find what the beginner requested, and correct the problem.
"""

import pandas as pd

students = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul"],
"marks": [75, 85, 65]
})

"""
print(students['age']) will give error because
there is no age column in the students DataFrame.
Pandas can only select columns that actually exist. If we want marks, use students["marks"]; if we need age, we must add an "age" column first.
"""