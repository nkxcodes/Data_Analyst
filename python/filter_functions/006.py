"""
Q6. — Medium
You have:
marks = [45, 82, 67, 91, 38, 76, 55]
Use filter() to keep only the students' marks that are 75 or higher.
Think about what the function given to filter() should return.
"""

marks = [45, 82, 67, 91, 38, 76, 55]

result = filter(lambda x: x >= 75, marks)

print(list(result))