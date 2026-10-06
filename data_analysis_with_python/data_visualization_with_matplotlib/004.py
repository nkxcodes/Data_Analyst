"""
Q4. — Medium
Create a bar chart showing the number of books read by four students:
Students: ["Aman", "Priya", "Rahul", "Neha"]
Books: [3, 5, 2, 7]
Add an appropriate title and axis labels.
Think about why a bar chart is more suitable than a line graph for this data.
"""

import matplotlib.pyplot as plt

students = ["Aman", "Priya", "Rahul", "Neha"]
books = [3, 5, 2, 7]

plt.bar(students, books)
plt.xlabel('Students')
plt.ylabel('Books')
plt.title('Books Read By Students')
plt.show()