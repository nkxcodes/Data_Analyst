"""
Q8. — Application
A school has this DataFrame:
marks = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha", "Karan"],
"maths": [75, 88, 62, 91, 54],
"science": [80, 92, 70, 89, 60]
})
The school wants to know which students scored more than 80 in Maths.
Select those students.
Do not manually inspect each student's marks.
"""

import pandas as pd

marks = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha", "Karan"],
"maths": [75, 88, 62, 91, 54],
"science": [80, 92, 70, 89, 60]
})

marks_above_80_in_maths = marks[marks['maths'] > 80] 

print(marks_above_80_in_maths)