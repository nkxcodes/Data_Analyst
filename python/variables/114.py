"""
Q14.​
Create a program that stores a list of numbers in a variable.
Use a loop and other variables to calculate the sum of all the numbers and the number of
elements in the list.
Finally, calculate the average.
"""


list_1 = [10, 20, 30, 40, 50, 60]

total_sum = 0
count = 0

for num in list_1:
    total_sum += num
    count += 1

average = total_sum / count

print(total_sum)
print(count)
print(average)