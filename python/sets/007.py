"""
Q7.​
Two students attended different days of a Python class.
Student A attended:
Monday, Tuesday, Wednesday, Friday
Student B attended:
Tuesday, Wednesday, Thursday, Friday
Use sets to determine:
●​ which days both students attended,
●​ which days only Student A attended,
●​ which days only Student B attended.
"""

student_a = {'Monday', 'Tuesday', 'Wednesday', 'Friday'}
student_b = {'Tuesday', 'Wednesday', 'Thursday', 'Friday'}

# ●​ which days both students attended,
print(student_a.union(student_b))

# ●​ which days only Student A attended,
print(student_a.difference(student_b))

# ●​ which days only Student B attended,
print(student_b.difference(student_a))