"""
Q15. — Mastery Challenge
You are given a small student performance dataset:
students = pd.DataFrame({ "name": ["Aman", "Priya", "Rahul", "Neha", "Karan",
"Riya",
"Arjun", "Meera"], "study_hours": [2, 4, 3, 5, 6, 1, 4, 6], "marks": [55, 72, 65, 84, 91, 45, 78,
95], "attendance": [70, 85, 80, 92, 96, 65, 88, 98]})
Create a small visual analysis that helps a teacher understand student performance.
Your analysis should explore:
●​ the relationship between study hours and marks
●​ how marks are distributed across students
●​ whether attendance and marks appear to be related
Choose appropriate visualizations, titles, labels, and other basic styling yourself.
You do not need to create three separate figures if a clear arrangement of plots would
communicate the results better.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

students = pd.DataFrame({ "name": ["Aman", "Priya", "Rahul", "Neha", "Karan", "Riya",
"Arjun", "Meera"], "study_hours": [2, 4, 3, 5, 6, 1, 4, 6], "marks": [55, 72, 65, 84, 91, 45, 78,
95], "attendance": [70, 85, 80, 92, 96, 65, 88, 98]})

plt.subplot(2, 2, 1)
sns.scatterplot(x='study_hours', y='marks', data=students, marker='x')

plt.subplot(2, 2, 2)
sns.histplot(x='marks', data=students)

plt.subplot(2, 2, 3)
sns.scatterplot(x='attendance', y='marks', data=students, marker='x')
plt.title('Study Hours vs Marks')
plt.xlabel('Study Hours')
plt.ylabel('Marks')

plt.show()