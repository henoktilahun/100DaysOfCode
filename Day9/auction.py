from art import logo
import os
clear = lambda: os.system('cls')

print(logo)
biddings = {}
biddings_finished = False

def highest_bidder(bidding_list):
    highest_bid = 0
    for bidder in bidding_list:
        bid_amount = bidding_list[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not biddings_finished:
    name = input("What is your name: ")
    bid = int(input("what is your bid: "))
    biddings[name] = bid
    other_bidders = input("Are there any other biders Y/N: ")
    if other_bidders == "N":
        biddings_finished = True
        highest_bidder(biddings)
    elif other_bidders== "Y":
        clear()

