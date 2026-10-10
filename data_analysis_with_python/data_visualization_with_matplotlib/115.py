"""
Q15. — Mastery Challenge
You are given this small student performance dataset:
students = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha", "Karan"],
"study_hours": [2, 4, 3, 5, 6],
"marks": [55, 72, 65, 84, 91]
})
Create a small visual analysis of the data.
Your visualization should help someone understand the relationship between study hours and
marks.
Make the graph clear enough that another student could look at it and understand the
information without reading your code.
You decide which type of visualization, labels, title, and other basic Matplotlib features are
appropriate.
"""

import matplotlib.pyplot as plt
import pandas as pd

students = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha", "Karan"],
"study_hours": [2, 4, 3, 5, 6],
"marks": [55, 72, 65, 84, 91]
})

plt.scatter(students['study_hours'], students['marks'], marker='x')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.title('Study Hours vs. Marks')
plt.grid(True)

plt.show()