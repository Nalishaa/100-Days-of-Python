# Print logo
from random import randint
from data_for_game import data
import art

def options():
    """Returns a number that acts like an index for the array."""
    candidate_1 = 0
    candidate_2 = 0
    while candidate_1 == candidate_2:
        candidate_1 = randint(0,50-1)
        candidate_2 = randint(0,50-1)
    return candidate_1,candidate_2

def follower_count(candidate1_,candidate2_):
    """Returns a number i.e the index of the Higher follower count element in the array."""
    if data[candidate1_]['follower_count'] > data[candidate2_]['follower_count']:
        return candidate1_
    else:
        return candidate2_

def higher_lower():

    one_candidate,two_candidate = options()
    score = 0

    game_end = False
    while not game_end:

        print(art.logo)

        if score > 0:
            print(f"You're right! Current score: {score}")

        print(f"Compare A: {data[one_candidate]['name']}, a {data[one_candidate]['description']}, from {data[one_candidate]['country']}.")

        print(art.vs)

        print(f"Against B: {data[two_candidate]['name']}, a {data[two_candidate]['description']}, from {data[two_candidate]['country']}.\n")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        if user_choice == 'A':
            user_answer = one_candidate
        else:
            user_answer = two_candidate

        correct_answer = follower_count(one_candidate,two_candidate)

        # Find out if the user choice is same as the higher one
        ## If yes then increase score and say correct. Then, switch the choices
        ## Else end the game and show total score

        print("\n" * 20)
        if user_answer == correct_answer:
            score += 1
            one_candidate = two_candidate
            two_candidate,_ = options()

        else:
            print(art.logo)
            print(f"Sorry that is wrong. Final Score: {score}")
            game_end = True

higher_lower()

