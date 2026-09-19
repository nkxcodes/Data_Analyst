"""
Q15. — Challenge
You are given:
products = [
("Laptop", 55000),
("Mouse", 800),
("Keyboard", 1500),
("Monitor", 12000),
("Headphones", 2500)
]
A store wants a list of products that are suitable for a special offer:
●​ The product must cost more than ₹1,000
●​ The original product information should remain unchanged.
Create the filtered result.
Decide yourself how filter() can naturally be used to solve the problem.
"""

products = [
("Laptop", 55000),
("Mouse", 800),
("Keyboard", 1500),
("Monitor", 12000),
("Headphones", 2500)
]

result = filter(lambda product: product[1] > 1000, products)

print(list(result))