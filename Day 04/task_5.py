import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options=[rock, paper, scissors]
user_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice>2 or user_choice<0:
    print("You've provided the wrong input.")
else:
    print(options[user_choice])
    print("Computer chose: ")
    comp_choice=random.randint(0,2)
    print(options[comp_choice])
    if user_choice==0 and comp_choice==2:
        print("You WIN!")
    elif user_choice==2 and comp_choice==1:
        print("You WIN!")
    elif user_choice==1 and comp_choice==0:
        print("You WIN!")
    elif user_choice==comp_choice:
        print("It's a draw.")
    else:
        print("You Lose.")

