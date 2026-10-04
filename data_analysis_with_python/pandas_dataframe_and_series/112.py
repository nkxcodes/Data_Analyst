"""
Q12. — Tricky
Given:
students = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [45, 72, 88, 35]
})
Predict what this condition produces:
students["marks"] > 60
Will it produce:
●​ one True/False value,
●​ a list,
●​ or a Pandas Series of Boolean values?
Then use the result to select the matching students.
"""

import pandas as pd

students = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [45, 72, 88, 35]
})

print(students['marks'] > 60) # Prints a Series of Boolean Values
print(students[students['marks'] > 60])