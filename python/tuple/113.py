"""
Q13.​
Create a tuple containing several numbers.
Use a loop and conditions to count how many numbers are:
●​ even
●​ odd
Do not change the original tuple.
"""

numbers = (12, 7, 4, 19, 8, 15, 22, 3, 10, 6)
even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print(f'Even numbers: {even}')
print(f'Odd numbers: {odd}')