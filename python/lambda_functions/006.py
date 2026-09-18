"""
Q6. — Medium
Look at these two approaches:
●​ A normal function that takes a number and returns its cube.
●​ A lambda function that does the same thing.
Write both yourself and compare them.
Think about: What is the main difference in how they are written and used?
"""

def cube(x):
    return x * x * x

result = cube(2)

print(result)

# Lambda:

cube =  lambda x: x * x * x

result_2 = cube(2)

print(result_2)