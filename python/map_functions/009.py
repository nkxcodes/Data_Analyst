"""
Q9. — Application
You have temperatures in Celsius:
celsius = [0, 10, 20, 30, 40]
Convert every temperature to Fahrenheit using:
F = (C × 9/5) + 32
Use map() to perform the conversion.
"""

celsius = [0, 10, 20, 30, 40]

result = map(lambda c: (c * 9/5) + 32, celsius)

print(list(result))