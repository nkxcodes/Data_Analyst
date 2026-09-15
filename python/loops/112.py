"""
Q12.​
Consider this program:
for number in range(1, 11):
if number == 6:
break
print(number)
Predict exactly what will be printed.
Then explain what break does to the loop.
After that, change the program so that 6 is skipped but the loop continues printing 7, 8, 9,
and 10.
"""
for number in range(1, 11):
    if number == 6:
        break
    print(number)

# The second change
for number in range(1, 11):
    if number == 6:
        continue
    print(number)