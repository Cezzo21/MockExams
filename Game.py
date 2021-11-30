import random

lives = 3
n = 5

for n in range(1,11):
    type = random.randint(1,4)
    #Game Over
    if lives == 0:
        print("GAME OVER!!!!")
        quit()
    #Multiplication
    elif type == 1:
        x = random.randint(1,12)
        y = random.randint(1,12)
        print(str(n) + ". What is", str(y), "*", str(x))
        z = (int(input("= ")))
        if z == x*y:
            print("CORRECT")
        else:
            print("WRONG! IT'S", x*y)
            lives -= 1
    #Division
    elif type == 2:
        x = random.randint(1, 12)
        y = x*random.randint(1, 5)
        print(str(n) + ". What is", str(y), "/", str(x))
        z = (int(input("= ")))
        if z == y/x:
            print("CORRECT")
        else:
            print("WRONG! IT'S", y/x)
            lives -= 1
    #Addition
    elif type == 3:
        x = random.randint(1, 12)
        y = random.randint(1, 12)
        print(str(n) + ". What is", str(y), "+", str(x))
        z = (int(input("= ")))
        if z == y + x:
            print("CORRECT")
        else:
            print("WRONG! IT'S", y+x)
            lives -= 1
    #Subtraction
    elif type == 4:
        x = random.randint(1, 12)
        y = random.randint(1, 12)
        print(str(n) + ". What is", str(y), "-", str(x))
        z = (int(input("= ")))
        if z == y - x:
            print("CORRECT")
        else:
            print("WRONG! IT'S", y-x)
            lives -= 1

#Scoring
print()
score = 7 + lives
print("FINAL SCORE:", str(score) + "/10")
if score == 10:
    print("You're a Math genius!")
if score == 9:
    print("Nerd")

#QUIT
quit()