"""
Q9. — Application
You have a list of student names:
["Rahul", "Aman", "Priya", "Alexander", "Neha"]
You want to arrange the names according to their length, from shortest to longest.
Use a lambda to tell Python what property of each name should be used for sorting.
"""

students = ['Rahul', 'Aman', 'Priya', 'Alexander', 'Neha']

students = sorted(students, key=lambda name: len(name))

print(students)