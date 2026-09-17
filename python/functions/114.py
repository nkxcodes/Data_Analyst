"""
Q14.
Create a function called find_passed_students() that receives:
●​ a list of student names
●​ a list of their corresponding marks
Return a new list containing the names of students who scored at least 50.
Make sure the names and marks stay correctly matched.
"""

def find_passed_students(students, marks):
    passed_students = []
    for num in marks:
        if num >= 50:
            passed_students.append(students[marks.index(num)])
    return passed_students

result = find_passed_students(["Rahul", "Aman", "Priya", "Neha"], [75, 42, 68, 35])

print(result)