"""
Q9. — Application
Given:
products = pd.DataFrame({
"product": ["Pen", "Notebook", "Bag", "Bottle"],
"price": [20, 80, 500, 250]
})
The shop increases every product's price by 10%.
Update the prices and display the DataFrame.
Think about how Pandas allows you to perform an operation on an entire column.
"""

import pandas as pd

products = pd.DataFrame({
"product": ["Pen", "Notebook", "Bag", "Bottle"],
"price": [20, 80, 500, 250]
})

products['price'] =  products['price'] + (products['price'] * 0.1)

print(products)