import random

choices = ["rock", "Paper", "Scissors"]

computer = random.choice(choices)
player = None


while player not in choices:
    player = input("rock , paper, or scissors?:").lower()

print("computer: ",computer)
print("player: ",player)

