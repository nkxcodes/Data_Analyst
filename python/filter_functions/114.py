"""
Q14. — Mixed
You have:
students = [
("Rahul", 78),
("Aman", 45),
("Priya", 91),
("Neha", 62),
("Rohan", 35)
]
Keep only the students who passed, where passing means marks are 50 or higher.
The resulting data should still contain the student's name and marks together.
"""

students = [
("Rahul", 78),
("Aman", 45),
("Priya", 91),
("Neha", 62),
("Rohan", 35)
]

result = filter(lambda student: student[1] >= 50, students)

print(list(result))