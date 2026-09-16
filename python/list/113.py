"""
Q13.​
Create a function that receives a list of numbers and returns the largest number in the list.
Do not simply use Python's built-in function for finding the maximum. Use a loop and a variable
to determine it yourself.
Test your function with different lists.
"""

def find_largest(u_list):
    largest = u_list[0]
    for num in u_list:
        if num > largest:
            largest = num
    return largest

result = find_largest([1, 2, 3, 4, 5, 87])

print(f'Largest: {result}')