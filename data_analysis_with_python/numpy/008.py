"""
Q8. — Application
A shop records the prices of five products:
[100, 250, 80, 300, 150]
Create a NumPy array and increase every price by 10%.
Print the new prices.
Think about why NumPy is useful for this type of operation.
"""

import numpy as np

products_prices = np.array([100, 250, 80, 300, 150])

increased_prices = products_prices + (products_prices * 0.1)

print(increased_prices)