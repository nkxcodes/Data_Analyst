"""
Q15.​
Imagine you are making a very small personal information program.The program should store information such as:
●​
●​
●​
●​
●​
name
age
city
favorite programming language
number of Python problems solved
Then use those variables to produce a short summary about the person.
You decide how to organize the variables and how to display the information. The goal is to
make the program easy to modify if any information changes.
"""

name = input('Enter your name: ')
age = int(input('Enter you age: '))
favorite_language = input('Enter your favourite programming language: ')
python_problems = int(input('Enter number of python problems solved: '))

summary = f"My name is {name}. I am {age} years old. My favorite programming language is {favorite_language}, and I have solved {python_problems} Python problems."

print(summary)