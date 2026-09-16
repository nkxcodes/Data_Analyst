"""
Q8.​
A shopping list contains several items.
Create a list of items you need to buy.
During shopping:
●​ one item becomes unnecessary,
●​ one new item is needed,
●​ and one existing item's position in the list needs to change.
Update the list accordingly and display the final shopping list.
"""

shopping = ["milk", "bread", "eggs", "rice", "apples"]

shopping.remove('eggs')
shopping.append('soap')

shopping.remove('apples')
shopping.insert(0, 'apples')

print(shopping)