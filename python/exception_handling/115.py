"""
Q15. — Challenge
Create a small Safe Student Marks Program.
The program should repeatedly ask the user to enter a student's mark.
It should:
accept valid integer marks
reject invalid input without crashing
handle marks outside a reasonable range such as 0–100
continue asking until the user chooses to stop
display the final valid marks entered
make sure any necessary cleanup/final message happens even if an error occurs
Use try, except, else, and finally where they naturally fit.
The goal is not to use every block just because you can—the goal is to understand what each
block is actually responsible for.
"""

is_running = True
marks_list = []

while is_running:
    try:
        marks = input('Enter marks: ')
        if marks == 'done':
            is_running = False
            print(marks_list)
            break
        marks = int(marks)
        if marks < 0 or marks > 100:
            print('Invalid Marks!')
            continue
    except ValueError:
        print('Invalid Marks!')
    else:
        marks_list.append(marks)
    finally:
        print('Execution completed!') 