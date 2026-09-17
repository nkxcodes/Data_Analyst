"""
Q12.
Predict the output of this program:
def change_number(number):
number = number + 10
return number
x=5
change_number(x)
print(x)
Then modify the program so that the changed value can actually be stored and used.
Explain why simply calling the function does not change the value stored in x.
"""

def change_number(number):
    number = number + 10
    return number

x = 5

result = change_number(x)

print(result)
print(x)

# number is a local variable in function, it takes the value of x only and use it in another variable.