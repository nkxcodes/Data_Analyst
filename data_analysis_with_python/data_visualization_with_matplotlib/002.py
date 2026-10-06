"""
Q2. — Easy
Create a line plot showing the temperature over five days:
Days: [1, 2, 3, 4, 5]
Temperature: [28, 30, 29, 32, 31]
Add:
●​ a title
●​ a label for the x-axis
●​ a label for the y-axis
"""

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
temperature = [28, 30, 29, 32, 31]

plt.plot(days, temperature)
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.title('Temperature Visualization')
plt.show()