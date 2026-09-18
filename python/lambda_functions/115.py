"""
Q15. — Challenge
You are given a list of products:
products = [
("Laptop", 55000),
("Mouse", 800),
("Keyboard", 1500),
("Monitor", 12000),
("Headphones", 2500)
]
Create a small program that displays the products from cheapest to most expensive.
Then modify your program so that it displays only products costing more than ₹2,000, while
keeping them ordered by price.
Decide yourself where a lambda function naturally fits into the solution.
"""

products = [
("Laptop", 55000),
("Mouse", 800),
("Keyboard", 1500),
("Monitor", 12000),
("Headphones", 2500)
]

expensive_products = []

products = sorted(products, key=lambda product: product[1])

print(products)

for product in products:
    if product[1] > 2000:
        expensive_products.append(product)

expensive_products = sorted(expensive_products, key=lambda product: product[1])

print(expensive_products)