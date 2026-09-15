"""
Q13.​
Create a function that receives a list of numbers and returns how many numbers in the list are
even.
For example, given:
[2, 7, 10, 13, 18, 21]
the function should return the number of even values.
Use a loop, condition, variable, and function.
"""

def count_even(u_list):
    even = 0
    for number in u_list:
        if number % 2 == 0:
            even += 1
    return even

result = count_even([2, 7, 10, 13, 18, 21])

print(result)