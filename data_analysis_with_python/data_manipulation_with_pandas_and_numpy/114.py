"""
Q14. — Mixed
You have customer information in one DataFrame and purchase information in another:
customers = pd.DataFrame({
"customer_id": [1, 2, 3, 4],
"name": ["Aman", "Priya", "Rahul", "Neha"],
"city": ["Delhi", "Mumbai", "Delhi", "Pune"]
})
purchases = pd.DataFrame({
"customer_id": [1, 1, 2, 3, 3],
"amount": [500, 200, 800, 300, 700]
})
Create a small analysis that determines:
●​ each customer's total purchase amount
●​ the city-wise total purchase amount
●​ the customer who spent the most
Think about the order in which you should merge, group, and aggregate the data.
"""

import pandas as pd

customers = pd.DataFrame({
"customer_id": [1, 2, 3, 4],
"name": ["Aman", "Priya", "Rahul", "Neha"],
"city": ["Delhi", "Mumbai", "Delhi", "Pune"]
})
purchases = pd.DataFrame({
"customer_id": [1, 1, 2, 3, 3],
"amount": [500, 200, 800, 300, 700]
})

customer_total_purchase_amount = pd.merge(customers, purchases, on='customer_id', how='inner').groupby('customer_id')['amount'].sum()
city_wise_purchase = pd.merge(customers, purchases, on='customer_id', how='inner').groupby('city')['amount'].sum()
most_spending_customer = customer_total_purchase_amount.idxmax()

print(customer_total_purchase_amount)
print(city_wise_purchase)
print(most_spending_customer)