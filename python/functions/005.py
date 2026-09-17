"""
Q5.
Create a function called introduce() that takes:
●​ name
●​ age
●​ country
It should display a short introduction using all three pieces of information.
Call the function using keyword arguments rather than relying only on their position.
"""

def introduce(name, age, country):
    print(f'Hi, My name is {name} of age {age} from {country}.')

introduce(name='Amit', age=17, country='India')