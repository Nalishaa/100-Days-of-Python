from art import logo
import random

def guess_the_number(level):
    number=random.randint(1,100)
    if level == 'easy':
        i = 10
    else:
        i = 5

    while i > 0:
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if i == 1 and guess != number:
            print("You've run out of guesses. Refresh the page to run again.")
        elif guess == number:
            print(f"You got it! The answer was {number}")
            return
        elif guess < number:
            print("Too low.\nGuess again.")
        elif guess > number:
            print("Too high.\nGuess again.")
        i-=1

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
guess_the_number(difficulty)