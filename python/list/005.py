"""
Q5.
Create a list of five fruits.
Then:
1. Change one fruit to a different fruit.
2. Add a new fruit to the list.
3. Remove one fruit from the list.
Print the list after each major change.
"""

fruits = ['Mango', 'Apple', 'Banana', 'Pear', 'Peach']
print(fruits)

fruits[3] = 'Pineapple'
print(fruits)

fruits.append('Kiwi')
print(fruits)

fruits.remove('Mango')
print(fruits)