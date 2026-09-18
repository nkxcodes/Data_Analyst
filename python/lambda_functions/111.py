"""
Q11. — Tricky
Find the mistake in this code:
square = lambda x:
x*x
The programmer wants a lambda that returns the square of a number.
Identify what is wrong and rewrite it correctly.
"""

square = lambda x: x * x # lambda expects the expression right after : .
