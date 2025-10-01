import art
import random

def deal_card():
    """"Returns a random card form the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    total= sum(cards)
    if len(cards) == 2 and total == 21:
        return 0
    elif 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return total

def compare(score_user, score_comp):
    if score_user == score_comp:
        print("It's a Draw.")
    elif score_comp == 0:
        print("You lose.")
    elif score_user > 21:
        print("You went over. You lose.")
    elif score_comp > 21:
        print("Opponent went over. You win.")
    else:
        if score_user > score_comp:
            print("You win.")
        else:
            print("You lose.")

def blackjack():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play == 'y':
        print("\n" * 20)
        print(art.logo)
        game_end=False
        user_cards = []
        computer_cards = []
        for i in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
    else:
        return

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]} ")

    if user_score == 0:
        user_score=21
        print("Player--Blackjack. You win.")
        blackjack()
        return

    elif computer_score == 0:
        computer_score=21
        print("Opponent--Blackjack. You lose.")
        blackjack()
        return

    elif user_score > 21 or computer_score > 21:
        blackjack()
        return

    while not game_end:
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        another_card=input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            if user_score >= 21:
                game_end = True
            else:
                print(f"Your cards: {user_cards}, current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]} ")

        else:
            game_end = True

    print(f"Your final hand: {user_cards}, final score: {user_score} ")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score} ")
    compare(user_score, computer_score)
    blackjack()

blackjack()


