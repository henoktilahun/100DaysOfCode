from art import logo
import random


print(logo)

def game_level(difficulty_level):
    if difficulty_level == "easy":
        turns = 10
    elif difficulty_level == "hard":
        turns = 5
    
    return turns


def play_game():
    random_number = random.randint(1,101)
    difficulty_level = input('Please choose a game mode by typing "easy" or "hard": ')
    turns = game_level(difficulty_level)
    print(f"You have {game_level(difficulty_level)} turns left" )
    while turns > 0:
        player_guess = int(input("Please guess a number between 1 and 100: "))
        if player_guess < random_number:
            print("Too low")
        elif player_guess > random_number:
            print("Too High")
        elif player_guess == random_number:
            print(f"Correct! number is {random_number}")
            break
        else:
            print(f"Wrong! your guess is {player_guess} and number is {random_number}")
        turns -= 1
        print(f"Turn left: {turns}")
    print("Game Over! out of turns")



play_game()


