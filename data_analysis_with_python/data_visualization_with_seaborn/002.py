"""
Q2. — Easy
Create this DataFrame:
students = pd.DataFrame(
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [72, 85, 64, 91]
)
Create a bar plot comparing the marks of the four students.
Make sure the student names appear on the horizontal axis and their marks on the vertical axis.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

students = pd.DataFrame({
    "name": ['Aman', 'Priya', 'Rahul', 'Neha'],
    "marks": [72, 85, 64, 91]
})

sns.barplot(x='name', y='marks', data=students)
plt.xlabel('Name')
plt.ylabel('Marks')
plt.title('Students Marks')

plt.show()