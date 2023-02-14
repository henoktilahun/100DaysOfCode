#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


from art import logo
import random


print(logo)


turns = 0

while turns < 5:
    print(f"Turn: {turns}")
    player_guess = int(input("Please guess a number between 1 and 100: "))
    random_number = random.randint(1,101)
    if player_guess < 1:
        print("Too low")
    elif player_guess > 100:
        print("Too High")
    elif player_guess == random_number:
        print(f"Correct! number is {random_number}")
    else:
        print(f"Wrong! your guess is {player_guess} and number is {random_number}")
    turns += 1