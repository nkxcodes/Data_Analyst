"""
Q7. — Application
A shop has these product prices:
prices = [500, 1200, 2500, 800, 3000, 1500]
The shop wants to display only products that cost more than ₹1,000.
Create the filtered result.
"""

prices = [500, 1200, 2500, 800, 3000, 1500]

result = filter(lambda x: x > 1000, prices)

print(list(result))