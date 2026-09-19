"""
Q4. — Medium
Create a normal function called cube() that takes one number and returns its cube.
Then use map() with that function to create cubes for:
[1, 2, 3, 4, 5]
"""

numbers = [1, 2, 3, 4, 5]

def cube(number):
    return number * number * number

result = map(cube, numbers)

print(list(result))