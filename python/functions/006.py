"""
Q6.
Create a function called calculate_total() that takes a price and quantity.
Give the quantity a default value of 1.
Test the function both:
●​ with a quantity provided
●​ without providing a quantity
Observe how the default value behaves.
"""

def calculate_total(price, quantity=1):
    return price * quantity

result = calculate_total(599, 3)
result_2 = calculate_total(599)

print(result)
print(result_2)