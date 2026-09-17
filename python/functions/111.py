"""
Q11.
Find and fix the mistake in this function:
def multiply(a, b):
result = a * b
print(multiply(5, 4))
The programmer expects the output to be 20.
After fixing it, explain why the original function did not give the expected result.
"""

def multiply(a, b):
    return a * b

print(multiply(5, 4))
"""
Original function did not give the expected result
beause there is neither a print statement nor return
inside function, it just creates a variables and stores result in 
local scope.
"""