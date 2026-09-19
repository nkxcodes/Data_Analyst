"""
Q7. — Application
A teacher has recorded these marks:
marks = [45, 67, 32, 89, 76]
The teacher wants to add 5 grace marks to every student's marks.
Create the new results using an appropriate map() approach.
"""

marks = [45, 67, 32, 89, 76]

result = map(lambda x: x + 5, marks)

print(list(result))