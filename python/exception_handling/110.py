"""
Q10. — Tricky
Predict the output without running the code:
try:
print("A")
x = 10 / 0
print("B")
except ZeroDivisionError:
print("C")
else:
print("D")
finally:
print("E")
Write the exact order in which the letters are printed.
Then explain why B and D are or are not executed.
"""

try:
    print('A')
    x = 10 / 0
    print('B')
except ZeroDivisionError:
    print('C')
else:
    print('D')
finally:
    print('E')

"""
prints:
A
C
E

B and D is not executed because B is there after the error.
after when error has been found control directly does to
except block. so, b is not executed.

D is not executed because program or try block is not successfull
is has an error, else block is not executed because of this reason.
else block is executed when there is no error in try.
"""