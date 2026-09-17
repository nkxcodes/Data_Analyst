"""
Q7.
You are creating a small shopping program.
Create a function that receives the prices of several items and calculates their total cost.
Use the function in a small program where the user can provide different prices and get the
total.
Think about what the function should receive and what it should return.
"""

def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

result = calculate_total({29, 49, 69, 89, 79})

print(result)