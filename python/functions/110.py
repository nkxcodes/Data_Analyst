"""
Q10.
Predict what this program will do before running it:
def calculate():
x = 10
y = 20
return x + y
result = calculate()
print(result)
print(x)
Run it afterward.
Explain why the first print() works but the second one causes a problem.
"""

def calculate():
    x = 10
    y = 20
    return x + y

result = calculate()

print(result)
# print(x) # Gives Error - because x is with the range of calculate function, we cannot access it outside function.