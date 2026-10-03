"""
Q4. — Medium
Write a program that tries to access the fifth element of this list:
numbers = [10, 20, 30]
Handle the appropriate exception so the program continues running instead of crashing.
"""

numbers = [10, 20, 30]

try:
    fifth_element = numbers[5]
except IndexError:
    print('Cannot able access fifth element, it does not exists!')
else:
    print(fifth_element)
finally:
    print('Execution completed!')