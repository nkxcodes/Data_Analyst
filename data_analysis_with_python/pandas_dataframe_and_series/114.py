"""
Q14. — Mixed
You have:
students = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha", "Karan"],
"marks": [72, 45, 88, 35, 91]
})
Using Pandas and a condition:
●​ find students who scored at least 50
●​ find the average marks of all students
●​ find the highest marks
Try to perform the analysis without using a for loop.
"""

import pandas as pd

students = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha", "Karan"],
"marks": [72, 45, 88, 35, 91]
})

at_least_50 = students[students['marks'] >= 50]
average_marks = students['marks'].mean()
highest_marks = students['marks'].max()

print(at_least_50)
print(average_marks)
print(highest_marks)