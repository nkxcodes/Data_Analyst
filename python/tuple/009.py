"""
Q9.​
Create a tuple containing the names of several students.
Use a loop to go through the tuple and display each student's name.
Then use a condition to display only the names that meet a condition you choose, such as
names longer than 5 characters.
"""

students = ("Rahul", "Aman", "Nitesh", "Priya", "Aditya", "Karan", "Sakshi")

for student in students:
    print(student)

print()
for student in students:
    if len(student) > 5:
        print(student)