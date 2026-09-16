"""
Q6.​
Create a list containing some repeated numbers, such as:
[10, 20, 10, 30, 40, 10, 50]
Find out:
●​ how many elements are in the list
●​ how many times 10 appears
●​ the position of the first 30
●​ whether 40 exists in the list
Use the appropriate list operations or built-in functions.
"""

numbers = [10, 20, 10, 30, 40, 10, 50]

count = 0
for num in numbers:
    count += 1

print(count)

count = 0
for num in numbers:
    if num == 10 :
        count += 1

print(count)

position = numbers.index(30)
print(position)

print(40 in numbers)