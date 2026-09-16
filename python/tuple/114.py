"""
Q14.​
Create a function that receives a tuple of numbers and returns the largest number in that tuple.
Test the function with different tuples.
Think about what should happen if the tuple contains negative numbers as well.
"""

def find_largest(u_tuple):
    largest = u_tuple[0]
    for num in u_tuple:
        if num > largest:
            largest = num
    return largest

result = find_largest((-23, -36, -65, -76, -87))

print(result)