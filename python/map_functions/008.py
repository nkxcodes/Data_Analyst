"""
Q8. — Application
A shop stores product names in lowercase:
products = ["laptop", "mouse", "keyboard", "monitor"]
The shop wants to display every product name with its first letter capitalized.
Use map() to transform the list.
"""

products = ['laptop', 'mouse', 'keyboard', 'monitor']

result = map(lambda product: product.capitalize(), products)

print(list(result))