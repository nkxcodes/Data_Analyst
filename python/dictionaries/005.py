"""
Q5.​
Create a dictionary containing five students and their marks.
Find and display:
●​ all the student names,
●​ all the marks,
●​ the number of students.
Use appropriate dictionary operations/methods rather than manually writing each value.
"""

students = {
    "Rahul": 85,
    "Aman": 92,
    "Priya": 78,
    "Manav": 45,
    "Somya": 56
}

# Print all student names.
for name in students:
    print(name)

print(students.keys())

# Print all marks.
for marks in students.values():
    print(marks)

print(students.values())

# Print the number of students.
print(len(students))