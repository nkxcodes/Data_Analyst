"""
Q7. — Application
You have this list:
[2, 4, 6, 8, 10]
You want a new list containing the square of every number.
Use a lambda-based approach to transform the values.
"""

numbers = [2, 4, 6, 8, 10]

squares = []

give_square = lambda x: x ** 2

for num in numbers:
    num = give_square(num)
    squares.append(num)

print(squares)