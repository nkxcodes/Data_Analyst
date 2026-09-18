"""
Q12. — Tricky
Consider:
add = lambda x, y: x + y
result = add(10, 20)
print(result)
Now answer these questions without changing the code:
1.​ What are x and y?
2.​ What are 10 and 20?
3.​ What does result contain?
4.​ Why can't you call add(10) successfully?
"""

add = lambda x, y: x + y

result = add(10, 20)

print(result)

"""
1. What are x and y:
    x and y are parameters which add function expects from user.

2. What are 10 and 20:
    10 and 20 are arguments to the add function by user.

3. What does result contain?:
    result contains the return result or the addition of provided two numbers by the function.

4. Why can't you call add(10) successfully?:
    because add function is designed to accept or expect two arguments from user.
"""