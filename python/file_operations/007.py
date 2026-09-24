"""
Q7. — Application
You have a file called students.txt containing one student's name on each line.
Create a program that reads the file and displays:
●​ the total number of students
●​ every student's name
Think about how you should process the file line by line.
"""

with open('students.txt', 'r') as file:
    reader = file.read()
    reader = reader.split('\n')

    total_students = 0
    for line in reader:
        total_students += 1

    print(f'Total Students: {total_students}')
    
    for student in reader:
        print(student)