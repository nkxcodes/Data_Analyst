"""
Q13. — Mixed
Create your own module containing a function that takes a list of numbers and returns their
total.
Then create a separate Python program that:
1.​ creates a list of numbers,
2.​ imports your function,
3.​ uses the function,
4.​ prints the result.
This combines modules, functions, variables, and lists.
"""

from module import total

numbers = [1, 2, 3, 4, 5]

result = total(numbers)

print(result)