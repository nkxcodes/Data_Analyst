"""
Q7. — Application
A shop has this sales data:
sales = pd.DataFrame({
"product": ["Pen", "Pen", "Bag", "Bag", "Notebook", "Notebook"],
"quantity": [10, 20, 2, 3, 5, 8],
"price": [20, 20, 500, 500, 80, 80]
})
The shop owner wants to know how many units of each product were sold in total.
Find the answer using the DataFrame.
"""

import pandas as pd

sales = pd.DataFrame({
"product": ["Pen", "Pen", "Bag", "Bag", "Notebook", "Notebook"],
"quantity": [10, 20, 2, 3, 5, 8],
"price": [20, 20, 500, 500, 80, 80]
})

product_sales = sales.groupby('product')['quantity'].sum()

print(product_sales)