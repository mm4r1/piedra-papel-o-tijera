import random

options = ["rock", "paper", "scissors"]

def choose_computer():
    return random.choice(options)

def decide_winner(player, computer):
    if player == computer:
        return "tie"
    elif player == "rock" and computer == "scissors":
        return "win"
    elif player == "scissors" and computer == "paper":
        return "win"
    elif player == "paper" and computer == "rock":
        return "win"
    else:
        return "lose"