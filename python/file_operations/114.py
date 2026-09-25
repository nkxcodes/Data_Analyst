"""
Q14. — Mixed
You have a file called students.csv containing:
Rahul,78
Aman,91
Priya,65
Neha,88
Rohan,72
Create a program that:
1.​ Reads the file.
2.​ Finds students who scored 75 or higher.
3.​ Writes those students into a new file called passed_students.txt.
The output file should contain the student's name and marks.
"""

with open('students_02.csv', 'r') as file:
    content = file.read()
    content = content.split('\n')
    
    with open('passed_students.txt', 'w') as file:
        for data in content:
            data = data.split(',')
            if int(data[1]) >= 75:
                file.write(f'{data[0]}\n{data[1]}\n')