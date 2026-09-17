"""
Q8.​
A shop has a dictionary containing products and their prices.
A customer gives you the name of a product.
Use the dictionary to determine whether the product exists and, if it does, display its price.
Think about how a dictionary makes this lookup easier than searching through a list manually.
"""

products = {
    "apple": 40,
    "milk": 60,
    "bread": 45,
    "rice": 80,
    "eggs": 70
}

search_request = input('Enter product: ')

print(products.get(search_request, 'Product not found.'))