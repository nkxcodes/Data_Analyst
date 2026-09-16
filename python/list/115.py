"""
Q15.​
Imagine you are building a small student marks management program.
Start with a list containing several students' marks.
Your program should:
●​ display the marks,
●​ add a new student's marks,
●​ remove an incorrect mark,
●​ calculate the total and average,
●​ count how many students passed,
●​ and display the highest mark.
"""

marks = [43, 54, 56, 76, 87, 87, 86, 98, 56, 76]

print(marks)
marks.append(89)
marks.remove(43)

total = 0
for num in marks:
    total += num

average = total / len(marks)

print(f'Total: {total}')
print(f'Average: {average}')

count = 0
for num in marks:
    if num >= 33:
        count += 1

print(f'Passed: {count}')

highest = marks[0]
for num in marks:
    if num > highest:
        highest = num

print(f'Highest: {highest}')