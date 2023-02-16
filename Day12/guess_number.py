from art import logo
from random import randint


print(logo)

EASY_TURN = 10
HARD_TURN = 5

def game_level():
    difficulty_level = input('Please choose a game mode by typing "easy" or "hard": ')
    if difficulty_level == "easy":
        return EASY_TURN
    elif difficulty_level == "hard":
        return HARD_TURN


def check_answer(player_guess, random_number, turns):
    """checks answer against player guess. Returns the number of turns remaining"""
    if player_guess < random_number:
        print("Too low")
        return turns - 1
    elif player_guess > random_number:
        print("Too High")
        return turns - 1
    else:
        print(f"Correct! number is {random_number}")


def play_game():
    random_number = randint(1,100)
    print(f"answer is {random_number}")
    turns = game_level()
    player_guess = 0
    while player_guess != random_number:
        print(f"You have {turns} turns left")
        player_guess = int(input("Please guess a number between 1 and 100: "))
        turns = check_answer(player_guess, random_number, turns)
        if turns == 0:
            print("You've run out of turns")
            return
        

play_game()