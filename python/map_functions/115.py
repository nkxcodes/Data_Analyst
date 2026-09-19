"""
Q15. — Challenge
You are given a list of student records:
students = [
("Rahul", 78),
("Aman", 91),
("Priya", 65),
("Neha", 88),
("Rohan", 72)
]
Create a program that produces a new result containing a simple message for every student,
such as:
Rahul scored 78 marks
The original students data should remain unchanged.
Decide yourself how map() can naturally be used to transform each student record into the
required message.
"""

students = [
("Rahul", 78),
("Aman", 91),
("Priya", 65),
("Neha", 88),
("Rohan", 72)
]

result = map(lambda student: f'{student[0]} scored {student[1]} marks', students)

print(list(result))