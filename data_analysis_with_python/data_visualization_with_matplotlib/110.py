"""
Q10. — Tricky — Predict first
Before running the code, predict what will happen:
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 30]
plt.plot(x, y)
plt.show()
Will the graph be created successfully?
If not, identify why the problem occurs.
Think about the relationship between the number of x-values and y-values.
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30]

plt.plot(x, y)
plt.show()

"""
The graph will not be created successfully because x contains
4 values, while y contains only 3 values.
Matplotlib requires both lists to have the same number
of values to pair each x-value with a corresponding
y-value. Therefor, it raises a ValueError.
"""