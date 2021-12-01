import random
player = 0
ai = 0

while player < 3 or ai < 3:
    weapon = random.randint(1, 3)
    print("Rock, Paper, Scissors, shoot!")
    user = str(input("- "))
    print("vs")
    #rock
    if weapon == 1 and (user == "Rock" or user == "rock"):
        print("- Rock")
        print("Tie")
    elif weapon == 1 and (user == "Paper" or user == "paper"):
        print("- Rock")
        print("You win!")
        player += 1
        print(player)
    elif weapon == 1 and (user == "Scissors" or user == "scissors"):
        print("- Rock")
        print("You lose!")
        ai += 1

    #Paper
    if weapon == 2 and (user == "Rock" or user == "rock"):
        print("- Paper")
        print("You lose!")
        ai += 1
    elif weapon == 2 and (user == "Paper" or user == "paper"):
        print("- Paper")
        print("Tie")
        print(player)
    elif weapon == 2 and (user == "Scissors" or user == "scissors"):
        print("- Paper")
        print("You win!")
        player += 1

    #Scissors
    if weapon == 3 and (user == "Rock" or user == "rock"):
        print("- Scissors")
        print("You win!")
        player += 1
    elif weapon == 3 and (user == "Paper" or user == "paper"):
        print("- Scissors")
        print("You lose!")
        ai += 1
        print(player)
    elif weapon == 3 and (user == "Scissors" or user == "scissors"):
        print("- Scissors")
        print("Tie")
    if player == 3 or ai == 3:
        break
score = str(int(player)) + " - " + str(int(ai))
print("GAME OVER: " + str(score))
quit()

