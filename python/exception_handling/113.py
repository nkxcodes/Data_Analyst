"""
Q13. — Mixed
Create a function called calculate_average() that receives a list of numbers.
The function should calculate the average, but the program should handle the situation where
the list is empty instead of crashing.
Then test the function with:
●​ a normal list of numbers
●​ an empty list
Combine functions, lists, numbers, and exception handling.
"""

def calculate_average(numbers):
    try:
        total = 0
        for num in numbers:
            total += num
        average = total / len(numbers)
    except ZeroDivisionError:
        print("It's an empty list!")
    else:
        print(f'Average: {average}')

calculate_average([1, 2, 3, 4, 5])
calculate_average([])