"""
Q9.​
You have a list of student marks.
Go through the list and create a new list containing only the marks that are 50 or higher.
The original list should remain unchanged.
"""

marks = [72, 85, 63, 91, 48, 76, 55, 89, 67, 94]

marks_50_or_higher = []

for i in marks:
    if i >= 50:
        marks_50_or_higher.append(i)

print(marks)
print(marks_50_or_higher)