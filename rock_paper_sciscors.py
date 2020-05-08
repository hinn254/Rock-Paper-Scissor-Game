'''
Winning rules are as follows:
Rock vs paper --> paper wins
Rock vs scissors --> Rock win
paper vs scissors --> scissors win 
'''

# import
import random

# print multiline instruction
print('Winning rules are as follows:\nRock vs paper --> paper wins\nRock vs scissors --> Rock winn\npaper vs scissors --> scissors win\n')

while True:
    print('Enter choice \n1. Rock\n2. Paper\n3. Scissor\n')

    # take input
    choice = int(input('User turn: '))

    while choice > 3 or choice < 1:
        choice = int(input('enter a valid input: '))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    elif choice == 3:
        choice_name = 'scissor'

    print('user choice is ' + choice_name)
    print('\nNow its computing turn......')

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'

    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name == 'scissor'

    print('computer choice is ' + comp_choice_name)

    # condition for winning
    if ((choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1)):
        print("paper wins => ", end='')
        result = 'paper'

    elif ((choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1)):
        print("rock wins => ", end='')
        result = 'Rock'
    else:
        print("scissors wins => ", end='')
        result = 'scissor'

    # Printing either user or computer wins
    if result == choice_name:
        print('<== user wins ==>')
    else:
        print('<== COmputer wins ==>')

    print('Do you want to play again? (y/n')
    ans = input().lower()

    if ans == 'n':
        break

print("\nThanks for playing")
