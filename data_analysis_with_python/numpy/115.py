"""
Q15. — Mastery Challenge
You are given the temperatures recorded during one week:
temperatures = np.array([28, 32, 35, 29, 38, 41, 33])
Create a small analysis that identifies:
●​ temperatures above 35
●​ temperatures between 30 and 35 inclusive
●​ temperatures below 30
Then calculate the average temperature.
Try to solve the whole problem using NumPy naturally, without manually checking each value
with a loop.
"""

import numpy as np

temperatures = np.array([28, 32, 35, 29, 38, 41, 33])

above_35 = temperatures[temperatures > 35]
between_30_35 = temperatures[(temperatures >= 30) & (temperatures <= 35)]
below_30 = temperatures[temperatures < 30]
average_temperature = temperatures.mean()

print(above_35)
print(between_30_35)
print(below_30)
print(average_temperature)