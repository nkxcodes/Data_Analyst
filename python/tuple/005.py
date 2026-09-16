"""
Q5.​
Create a tuple containing some repeated numbers, for example:
(10, 20, 10, 30, 10, 40)
Find out:
●​ how many elements are in the tuple
●​ how many times 10 appears
●​ the position of the first 30
Use the appropriate built-in operations or tuple methods.
"""

numbers = (10, 20, 10, 30, 10, 40)

print(len(numbers))

count = 0
for num in numbers:
    if num == 10:
        count += 1

print(f'10 Appeared {count} times.')

position = numbers.index(30)
print(f'Position of first 30 is {position}')