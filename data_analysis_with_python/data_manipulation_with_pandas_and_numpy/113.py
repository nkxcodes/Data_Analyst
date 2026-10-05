"""
Q13. — Mixed
Write a function that receives a sales DataFrame containing:
product
category
quantity
price
The function should create a new column representing the total value of each sale.
Then group the data by category and calculate the total sales value for each category.
Test your function with your own small DataFrame.
"""

import pandas as pd

sales = pd.DataFrame({
    "product": ["Pen", "Notebook", "Bag", "Pencil", "Notebook", "Bag"],
    "category": ["Stationery", "Stationery", "Accessories", "Stationery", "Stationery", "Accessories"],
    "quantity": [10, 5, 2, 20, 3, 1],
    "price": [20, 80, 500, 10, 80, 500]
})

def calculate_category_sales(sales):
    sales['total_value'] = sales['quantity'] * sales['price']
    each_category_sales =  sales.groupby('category')['total_value'].sum()
    return each_category_sales

each_category_sales = calculate_category_sales(sales)
print(each_category_sales)