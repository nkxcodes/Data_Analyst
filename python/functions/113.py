"""
Q13.
Create a function called count_even() that receives a list of numbers and returns how many
numbers are even.
For example, given:
[2, 7, 10, 13, 18, 21]
the function should return the number of even values.
Use a loop and condition inside the function.
"""

def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

result = count_even([2, 7, 10, 13, 18, 21])

print(result)