"""
Q5. — Medium
Create a lambda function that takes two numbers and returns the larger number.
Test it with:
●​ 10, 20
●​ 50, 30
●​ 7, 7
"""

find_larger = lambda x, y: x if x > y else y

result = find_larger(10, 20)
result_2 = find_larger(50, 30)
result_3 = find_larger(7, 7)

print(result)
print(result_2)
print(result_3)