"""
Q13.​
Create a function that receives a list of numbers and returns the number of unique values in
that list.
Test it with lists containing:
●​ no duplicates,
●​ some duplicates,
●​ all identical values.
"""

def unique_values(u_list):
    return len(set(u_list))

result = unique_values([1, 2, 3, 4, 5])
result_2 = unique_values([1, 2, 1, 3, 4, 4, 5])
result_3 = unique_values([1, 1, 1, 1, 1, 1])

print(result)
print(result_2)
print(result_3)