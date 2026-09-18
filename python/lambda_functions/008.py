"""
Q8. — Application
You have this list of numbers:
[3, 8, 11, 14, 17, 20, 25]
Create a new collection containing only the even numbers.
Use a lambda where it makes sense.
"""

numbers = [3, 8, 11, 14, 17, 20, 25]

even_numbers = []

is_even = lambda x: x % 2 == 0

for num in numbers:
    even = is_even(num)
    if even:
        even_numbers.append(num)

print(even_numbers)