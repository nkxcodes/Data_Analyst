"""
Q9. — Application
You receive two DataFrames:
customers = pd.DataFrame({
"customer_id": [101, 102, 103, 104],
"name": ["Aman", "Priya", "Rahul", "Neha"]
})
orders = pd.DataFrame({
"customer_id": [101, 102, 101, 103],
"amount": [500, 800, 300, 1000]
})
You want to connect each order with the corresponding customer's name.
Create a combined DataFrame containing the customer name and order amount.
The common column is customer_id.
"""

import pandas as pd

customers = pd.DataFrame({
"customer_id": [101, 102, 103, 104],
"name": ["Aman", "Priya", "Rahul", "Neha"]
})
orders = pd.DataFrame({
"customer_id": [101, 102, 101, 103],
"amount": [500, 800, 300, 1000]
})

customers_order_amount = pd.merge(customers, orders, on='customer_id', how='inner')

print(customers_order_amount)