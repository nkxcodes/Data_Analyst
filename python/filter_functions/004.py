"""
Q4. — Medium
Create a normal function called is_positive() that takes a number and determines whether
it is positive.
Then use filter() with that function to filter:
[-5, 3, -2, 8, 0, 10, -7]
"""

numbers = [-5, 3, -2, 8, 0, 10, -7]

def is_positive(number):
    return number > 0

result = filter(is_positive, numbers)

print(list(result))