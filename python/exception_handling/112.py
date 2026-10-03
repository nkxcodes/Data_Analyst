"""
Q12. — Tricky
Find the mistake in this code:
try:
number = int(input("Enter a number: "))
result = 100 / number
except Exception:
print("Something went wrong")
except ZeroDivisionError:
print("Cannot divide by zero")
The programmer wants ZeroDivisionError to receive its own specific message.
Explain why the exception handling does not behave as intended and how the order of the
handlers should be considered.
"""

try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception:
    print("Something went wrong")

"""
The mistake is that ZeroDivisionError is the second
exception, when error occurred in try block, control
is redirected to second except block.
"""