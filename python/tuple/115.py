"""
Q15.​
Imagine you are building a simple product information system.
Each product is represented by a tuple containing:
●​ product name
●​ price
●​ quantity
Create several product tuples and store them together in an appropriate structure.
Then process the products to calculate the total value of all products and display the product
information.
Decide yourself how you will organize and access the tuples.
"""

products = [
    ("Laptop", 50000, 2),
    ("Mouse", 500, 5),
    ("Keyboard", 1500, 3),
    ("Monitor", 12000, 2),
    ("Headphones", 2000, 4)
]

total_price = 0

for product in products:
    print(f'{product[0]}: {product[1]} x {product[2]} = {product[1] * product[2]}')
    total_price += product[1] * product[2]

print()
print(f'Total value: {total_price}')