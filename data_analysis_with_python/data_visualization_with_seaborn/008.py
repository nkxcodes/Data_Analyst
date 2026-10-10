"""
Q8. — Application
A school wants to compare the average marks of students across three subjects:
marks = pd.DataFrame({ "subject": ["Maths", "Maths", "Maths", "Science", "Science",
"Science",
"English", "English", "English"], "student": ["Aman", "Priya", "Rahul"] * 3,
"score": [80, 90, 70, 75, 85, 95, 88, 78, 82]})
Create a visualization that compares the average score for each subject.
The school wants to compare the subjects, not display every individual student's score.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

marks = pd.DataFrame({ "subject": ["Maths", "Maths", "Maths", "Science", "Science",
"Science",
"English", "English", "English"], "student": ["Aman", "Priya", "Rahul"] * 3,
"score": [80, 90, 70, 75, 85, 95, 88, 78, 82]
})

sns.barplot(x='subject', y='score', data=marks)
plt.title('Average Score by Subject')
plt.xlabel('Subject')
plt.ylabel('Average Score')

plt.show()