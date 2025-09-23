## This is my approach to solving the list of TODOs.
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
display=[]
for i in range(len(placeholder)):
    display += placeholder[i]

guess=[]
while "_" in display:
    guess += input("Guess a letter: ").lower()

# TODO-2: Change the for loop so that you keep the previous correct letters in display.
    for i in range(len(chosen_word)):
        for j in range(len(guess)):
            if chosen_word[i]==guess[j]:
                display[i]=guess[j]

    final_string=""
    for item in display:
        final_string+=item
    print(final_string)
print("You win!")


## Provided by the course
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
game_over=False
correct_letters=[]

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    # TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display += "_"

    print(display)
    if "_" not in display:
        game_over=True
        print("You win!")