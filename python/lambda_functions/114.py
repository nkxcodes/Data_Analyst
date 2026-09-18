"""
Q14. — Mixed
You have:
students = [
("Rahul", 82),
("Aman", 65),
("Priya", 91),
("Neha", 74),
("Rohan", 88)
]
Arrange the students according to their marks from highest to lowest.
Use a lambda to specify what part of each tuple should determine the ordering.
"""

students = [
("Rahul", 82),
("Aman", 65),
("Priya", 91),
("Neha", 74),
("Rohan", 88)
]

students = sorted(students, key=lambda student: student[0], reverse=True)

print(students)