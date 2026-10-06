"""
Q5. — Medium
Create a scatter plot using:
hours = [1, 2, 3, 4, 5, 6]
marks = [45, 50, 58, 65, 72, 80]
Add a title and labels.
Look at the graph and think about whether there appears to be a relationship between study
hours and marks.
"""

import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
marks = [45, 50, 58, 65, 72, 80]

plt.scatter(hours, marks)
plt.xlabel('Hours')
plt.ylabel('Marks')
plt.title('Study Hours vs Marks')
plt.show()