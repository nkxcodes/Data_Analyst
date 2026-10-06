"""
Q3. — Easy
Create a line plot using:
x = [1, 2, 3, 4, 5]
y = [5, 8, 6, 10, 12]
Add a grid to the graph.
Then change the appearance of the line using a different line style or marker.
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 8, 6, 10, 12]

plt.plot(x, y, linestyle='--', marker='o')
plt.grid(True)
plt.show()