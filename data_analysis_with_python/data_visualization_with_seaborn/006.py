"""
Q6. — Medium
Create a DataFrame:
students = pd.DataFrame({
90]})
"class": ["A", "A", "A", "B", "B", "B"],
"marks": [65, 75, 85, 60, 80,
Create a plot that compares the distribution of marks between classes A and B.
Your graph should help someone compare both the typical marks and the variation in marks
between the classes.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

students = pd.DataFrame({
    "class": ['A', 'A', 'A', 'B', 'B', 'B'],
    "marks": [65, 75, 85, 60, 80, 90]
})

sns.boxplot(x='class', y='marks', data=students)
plt.title('Distribution of Marks by Class')
plt.xlabel('Class')
plt.ylabel('Marks')

plt.show()