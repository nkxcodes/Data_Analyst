"""
Q15. — Mastery Challenge
You are given three small datasets:
customers = pd.DataFrame({
"customer_id": [101, 102, 103, 104],
"name": ["Aman", "Priya", "Rahul", "Neha"],
"city": ["Delhi", "Mumbai", "Delhi", "Pune"]
})
orders = pd.DataFrame({
"order_id": [1, 2, 3, 4, 5],
"customer_id": [101, 102, 101, 103, 104],
"amount": [500, 800, 300, 1000, 600]
})
extra = pd.DataFrame({
"customer_id": [101, 102, 103, 104],
"age": ["17", "18", "17", "19"]
})
Perform a small data-cleaning and analysis task:
combine the customer information with the extra customer information
make sure age has an appropriate numeric datatype
connect the customer information with their orders
find the total amount spent by each customer
find the average, highest, and lowest order amount for each customer
identify which city has the highest total sales
You should decide yourself where missing-value handling, datatype conversion, merging,
grouping, and multiple aggregation functions are useful.
"""

import pandas as pd

customers = pd.DataFrame({
"customer_id": [101, 102, 103, 104],
"name": ["Aman", "Priya", "Rahul", "Neha"],
"city": ["Delhi", "Mumbai", "Delhi", "Pune"]
})
orders = pd.DataFrame({
"order_id": [1, 2, 3, 4, 5],
"customer_id": [101, 102, 101, 103, 104],
"amount": [500, 800, 300, 1000, 600]
})
extra = pd.DataFrame({
"customer_id": [101, 102, 103, 104],
"age": ["17", "18", "17", "19"]
})

customer_information = pd.merge(customers, extra, on='customer_id', how='inner')
customer_information['age'] = customer_information['age'].astype(int)
customer_orders_information = pd.merge(customers, orders, on='customer_id', how='inner')
total_amount_spent_by_each = pd.merge(customers, orders, on='customer_id', how='inner').groupby('customer_id')['amount'].sum()
amount_analysis = pd.merge(customers, orders, on='customer_id', how='inner').groupby('customer_id')['amount'].aggregate(['mean', 'max', 'min'])
city_with_highest_total_sales = customer_orders_information.groupby('city')['amount'].sum().idxmax()

print()
print('Customer Information')
print('--------------------')
print(customer_information)

print()
print('Customer Orders')
print('--------------------')
print(customer_orders_information)

print()
print('Total Amount Spent')
print('--------------------')
print(total_amount_spent_by_each)

print()
print('Order Amount Analysis')
print('--------------------')
print(amount_analysis)

print()
print(f'City with highest total sales is {city_with_highest_total_sales}')