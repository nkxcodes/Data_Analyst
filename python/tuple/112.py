"""
Q12.​
Predict the output of this program before running it:
data = (10, 20, (30, 40), 50)
print(data[2])
print(data[2][0])
Then explain how Python is accessing the nested tuple.
"""

data = (10, 20, (30, 40), 50)

print(data[2]) # (30, 40)
print(data[2][0]) # 30

# A tuple can contain another tuple. This is called nested tuple.