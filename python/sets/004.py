"""
Q4.​
Create an empty set.
Then add three numbers to it one at a time.
After that, remove one of the numbers and print the final set.
"""
# set() is used to create empty set, otherwise with this {} python take it as dictionary.
numbers = set()

numbers.add(89)
numbers.add(45)
numbers.add(34)

numbers.remove(34)

print(numbers)