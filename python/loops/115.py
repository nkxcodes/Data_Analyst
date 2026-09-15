"""
Q15.​
Create a small number guessing game.
The program should have a secret number stored in a variable.
The user repeatedly enters guesses. After each guess, tell the user whether their guess is:
●​ too high
●​ too low
●​ correct
When the user guesses correctly, the program should stop and display a success message.
Decide yourself how to organize the loop, conditions, and variables.
"""
secret_number = 65
is_running = True

print('Welcome to number guessing game!.')
print()

while is_running:
    number = int(input('Guess number: '))
    if number == 0:
        is_running = False
    if number < secret_number:
        print('Too low')
    elif number > secret_number:
        print('Too high')
    else:
        print('Correct!')
        is_running = False
