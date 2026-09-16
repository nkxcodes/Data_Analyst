"""
Q14.​
Create a program that receives a list of numbers.
Use a loop and conditions to create two new lists:
●​ one containing the even numbers
●​ one containing the odd numbers
For example, if the original list contains:
[2, 7, 10, 13, 18, 21]
the two new lists should contain the appropriate numbers.
"""

numbers = [2, 7, 10, 13, 18, 21]
even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(numbers)
print(f'Even numbers: {even_numbers}')
print(f'Odd numbers: {odd_numbers}')