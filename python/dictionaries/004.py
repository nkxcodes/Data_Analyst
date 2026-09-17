"""
Q4.​
Create a dictionary representing a product with:
●​ name
●​ price
●​ quantity
Then:
1.​ Change the price.
2.​ Change the quantity.
3.​ Add a new key containing the product's category.
Print the final dictionary.
"""

product = {
    "name": "Headphones",
    "price": 499,
    "quantity": 1
}

# 1.​ Change the price.
product["price"] = 599

# 2.​ Change the quantity.
product["quantity"] = 2

# 3.​ Add a new key containing the product's category.
product["category"] = 'Electronics'

print(product)