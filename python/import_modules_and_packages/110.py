"""
Q10. — Tricky
Predict what happens when this code runs:
import math
print(math.sqrt(25))
print(sqrt(25))
One line works differently from the other.
Explain why.
"""

import math

print(math.sqrt(25))
# print(sqrt(25))

# the problem is how we imported sqrt
# import math imports whole module
# but this sqrt() give us error because it is not defined in our current scope.