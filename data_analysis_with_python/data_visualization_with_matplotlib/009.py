"""
Q9. — Application
A student's marks in five subjects are:
subjects = ["Maths", "Science", "English", "Computer", "History"]
marks = [82, 76, 91, 95, 68]
Create a suitable visualization.
Make sure that someone looking at your graph can quickly understand:
●​ which subject has the highest marks
●​ which subject has the lowest marks
●​ the marks for each subject
"""

import matplotlib.pyplot as plt

subjects = ["Maths", "Science", "English", "Computer", "History"]
marks = [82, 76, 91, 95, 68]

plt.bar(subjects, marks, color='purple')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Marks by Subject')
plt.show()