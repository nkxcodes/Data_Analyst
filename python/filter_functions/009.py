"""
Q9. — Application
You have a list of temperatures:
temperatures = [18, 25, 32, 12, 29, 35, 20]
A program needs to identify temperatures that are 30°C or higher.
Use an appropriate filtering approach.
"""

temperatures = [18, 25, 32, 12, 29, 35, 20]

result = filter(lambda x: x >= 30, temperatures)

print(list(result))