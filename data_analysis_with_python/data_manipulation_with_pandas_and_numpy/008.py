"""
Q8. — Application
Using the same sales DataFrame, the shop owner now wants to know for each product:
●​ total quantity sold
●​ average price
●​ highest price
Produce one grouped result containing all three pieces of information.
Think about how you can apply multiple aggregation functions to grouped data.
"""

import pandas as pd

sales = pd.DataFrame({
"product": ["Pen", "Pen", "Bag", "Bag", "Notebook", "Notebook"],
"quantity": [10, 20, 2, 3, 5, 8],
"price": [20, 20, 500, 500, 80, 80]
})

result = sales.groupby('product').aggregate({
    'quantity': 'sum',
    'price': ['mean', 'max']
})

print(result)