"""
Q15. — Mastery Challenge
You are given the following small sales dataset:
sales = pd.DataFrame({
"product": ["Pen", "Notebook", "Pen", "Bag", "Notebook", "Bag"],
"quantity": [10, 5, 20, 2, 8, 3],
"price": [20, 80, 20, 500, 80, 500]
})
Create a small analysis of this data.
Your program should determine:
the total number of items sold
the total sales amount
which sales records have a value greater than 500
the product names involved in those larger sales
Use Pandas naturally. Don't manually calculate each row.
"""

import pandas as pd

sales = pd.DataFrame({
"product": ["Pen", "Notebook", "Pen", "Bag", "Notebook", "Bag"],
"quantity": [10, 5, 20, 2, 8, 3],
"price": [20, 80, 20, 500, 80, 500]
})

number_of_items_sold = sales['quantity'].sum()

sales['sales_amount'] = sales['quantity'] * sales['price']
total_sales_amount = sales['sales_amount'].sum()

print()
print(f'Number of Items Sold: {number_of_items_sold}')

print()
print(f'Total Sales Amount: {total_sales_amount}')

print()
print(f'Sales Amount Above 500: \n {sales[sales['sales_amount'] > 500]}')

large_sales = sales[sales['sales_amount'] > 500]
print()
print(large_sales['product'])