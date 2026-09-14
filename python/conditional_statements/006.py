"""
Q6.​
Create a program that takes a student's marks and assigns a grade:
●​ 90 or above → A
●​ 75–89 → B
●​ 50–74 → C
●​ below 50 → F
Think carefully about the order in which your conditions should be checked.
"""

marks = input('Enter Marks: ')

grade = ''

if marks >= 90:
    grade = 'A'
elif marks >= 75 and marks <= 89:
    grade = 'B'
elif marks >= 50 and marks <= 74:
    grade = 'C'
elif marks < 50:
    grade = 'F'

print(f'Grade = {grade}')