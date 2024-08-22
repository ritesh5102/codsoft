import random


print(" Welcome to Rock, Paper, Scissor game")

options = ["Rock", "Paper", "Scissor"]
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
           player = input("Enter your choice ( Rock, Paper, Scissor): ")

    print(f"PLayer: {player}")
    print(f"Computer:  {computer}")

    if player == computer:
        print(" It is a draw")
    if player == "Rock" and computer == "Paper":
        print("You lose")
    elif player == "Paper" and computer == "Rock":
        print("You win")
    elif player == "Scissor" and computer == "Rock":
        print("You lose")
    elif player == "Scissor" and computer == "Paper":
        print("You win")
    elif player == "Rock" and computer == "Scissor":
        print("You win")
    elif player == "Paper" and computer == "Scissor":
        print("You lose")
    else:
        print("You lose")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")