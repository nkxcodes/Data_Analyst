"""
Q13. — Mixed
You have:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Create a new list containing the squares of only the even numbers.
You may combine lambda functions with concepts you already learned.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares_of_even = []

is_even = lambda x: x % 2 == 0
give_square = lambda x: x ** 2

for num in numbers:
    even = is_even(num)
    if even:
        square = give_square(num)
        squares_of_even.append(square)

print(squares_of_even)