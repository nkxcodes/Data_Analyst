"""
Q15.​
Create a small student record system using a dictionary.
Each student should have information such as:
●​ name
●​ age
●​ marks
●​ city
Your program should allow you to:
add a student,
update a student's marks,
look up a student's information,
determine whether the student passed,
and display the stored student records.
Decide yourself how the dictionary should be structured so that these operations are simple to
perform.
"""

students = {}

students[1] = {"name": "Rahul", 
               "age": 17,
               "marks": 67,
               "city": "Delhi"}

print(students)

students[1]["marks"] = 98
print(students)

print(students[1])

if students[1]["marks"] >= 40:
    print(f'Passed')
else:
    print(f'Failed')

print(students)