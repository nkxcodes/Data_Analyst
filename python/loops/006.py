"""
Q6.
Create a program that calculates the sum of numbers from 1 to 100.

Do not calculate the answer manually. Use a loop and a variable to keep track of the total.
"""

total_sum = 0

for num in range(1, 101):
    total_sum += num

print(total_sum)