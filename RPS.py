import random
while True:
    choices = ["rock", "papers", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, papers, or scissors?: ").lower()
    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")
    elif player == "rock":
        if computer == "papers":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose! the computer laughs at you")
        if computer == "scissors":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose! the computer laughs at you")
        if computer == "papers":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
    elif player == "papers":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose! the computer laughs at you")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
    play_again = input("Play again? (y/n):").lower()

    if play_again == "n":
            break
print("Bye")