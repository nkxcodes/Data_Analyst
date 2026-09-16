"""
Q12.​
Predict the output of this program:
numbers = [5, 10, 15, 20, 25]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
Then explain what each slice is selecting.
After that, create your own list and test different slicing ranges.
"""

numbers = [5, 10, 15, 20, 25]

print(numbers[1:4]) # [10, 15, 20]
print(numbers[:3]) # [5, 10, 15]
print(numbers[2:]) # [15, 20, 25]

numbers_1 = [454, 434, 656, 767, 878, 989]

print(numbers_1[:4])
print(numbers_1[4:])
print(numbers_1[::-1])
