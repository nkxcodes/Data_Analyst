"""
Q4. — Medium
Given:
data = pd.DataFrame({
"study_hours": [1, 2, 3, 4, 5, 6],
"marks": [42, 50, 58, 67, 75, 88]})
Create a scatter plot showing the relationship between study hours and marks.
Add a title and appropriate axis labels.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.DataFrame({
"study_hours": [1, 2, 3, 4, 5, 6],
"marks": [42, 50, 58, 67, 75, 88]
})

sns.scatterplot(x='study_hours', y='marks', data=data, marker='x')
plt.title('Relationship Between Study Hours and Marks')
plt.xlabel('Study Hours')
plt.ylabel('Marks')

plt.show()