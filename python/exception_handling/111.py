"""
Q11. — Tricky
Predict what happens here:
try:
number = int("hello")
except ValueError:
print("Value error")
except Exception:
print("Some other error")
else:
print("Success")
finally:
print("Finished")
Answer:
1.​ Which except block runs?
2.​ Does the else block run?
3.​ Does the finally block run?
4.​ Why?
"""

try:
    number = int("hello")
except ValueError:
    print("Value error")
except Exception:
    print("Some other error")
else:
    print("Success")
finally:
    print("Finished")

"""
ValueError except block will run.
else block will not run because an exeception occured
in try block, so the else block is skipped.
produce a error.
finally block always executed whether there is a exception
or not.
"""