import random

gamesPlayed = 0
gamesWon = 0

while gamesPlayed < 3:
    playerChoice = input("Choose your Weapon (rock/paper/scissors): ")

    mylist = ["rock", "paper", "scissors"]
    rand = random.choice(mylist)

    gamesPlayed += 1

    match playerChoice:
        case "rock":
            if rand == "rock":
                print(
                    "It's a DRAW, your ROCK battles tirelessly against an equal competitor!"
                )
            elif rand == "paper":
                print("You LOSE! The PAPER-shield you face proves too strong!")
            else:
                print("YOU WIN!!! Your strong ROCK crushes the opponent's SCISSORS!")
                gamesWon += 1

        case "paper":
            if rand == "rock":
                print(
                    "YOU WIN! Your mighty PAPER-shield overpowers the opponent's ROCK!"
                )
                gamesWon += 1
            elif rand == "paper":
                print("DRAW! A fair match of equally strong forces, PAPER vs PAPER!")
            else:
                print(
                    "Oh no, you LOSE! The opponent's SCISSORS slice through your PAPER!"
                )

        case "scissors":
            if rand == "rock":
                print("Ah, you LOSE! Your opponent's ROCK crushes your SCISSORS!")
            elif rand == "paper":
                print("You WIN! Your sharp SCISSORS cut through the enemy's PAPER!")
                gamesWon += 1
            else:
                print("DRAW! Both SCISSORS clash with equal might!")

print(f"You won {gamesWon} out of 3 games!")
