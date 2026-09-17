"""
Q11.​
Find and fix the mistake in this program:
student = {
"name": "Nitesh",
"marks": 85
}
print(student["grade"])
The programmer wants to display the student's grade, but the dictionary does not contain that
information.
Fix the program so it handles this situation safely.
"""

student = {
    "name": "Nitesh",
    "marks": 85
}

print(student.get('grade', 'Grade not found.'))