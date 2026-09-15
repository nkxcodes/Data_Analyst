"""
Q11.​
Find and fix the mistake in this program:
number = 1
while number <= 5:
print(number)
The programmer wants the program to print:
1 2 3 4 5
and then stop.
After fixing it, explain why the original program does not stop.
"""

number = 1

while number <= 5:
    print(number)
    number += 1

"""
Original program does not stop because
number is 1 initial, now we are checking is it 
smaller than 5 but we never increased the value of number.
so number always stays zero and satisfy the condition of
number <= 5
"""