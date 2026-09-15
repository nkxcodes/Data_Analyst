"""
Q13.​
You have a list of numbers:
[12, -5, 0, 8, -2, 15]
Use a loop and conditional statements to examine every number and count how many are:
●​ positive
●​ negative
●​ zero
"""

number = [12, -5, 0, 8, -2, 15]
positive = 0
negative = 0
zero = 0

for num in number:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print(f'Positive: {positive}')
print(f'Negative: {negative}')
print(f'Zero: {zero}')