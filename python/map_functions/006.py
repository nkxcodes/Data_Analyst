"""
Q6. — Medium
You have two lists:
prices = [100, 200, 300, 400]
quantities = [2, 3, 1, 5]
Use map() to calculate the total price for each item by combining the corresponding price and
quantity.
For example, the first result should represent:
100 × 2
"""

prices = [100, 200, 300, 400]
quantities = [2, 3, 1, 5]

result = map(lambda x, y: x * y, prices, quantities)

print(list(result))