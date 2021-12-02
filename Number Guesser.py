import random
again = "yes"

while again == "yes":
    #reset the range
    min = 1
    max = 100
    five = 0
    four = 0
    three = 0
    two = 0
    print("--- N U M B E R   G U E S S E R ---")
    #input
    while True:
        try:
            x = int(input("Think of a number 1 to 100 (I won't look I promise): "))
            if x < 1 or x > 100:
                print("I said 1 to 100 >:(")
            else:
                print("cool cool cool. I'm thinking...")
                break

        except:
            print("OK I looked. Give me an integer please. We don't wanna go forever!")
    while True:
        guess = random.randint(min, max)
        print("I'm thinking of", guess)
        #difference
        if guess < x:
            diff = x - guess
        elif guess > x:
            diff = guess - x
        elif guess == x:
            diff = 10

        #close
        if diff <= 5 and guess < x and five == 0:
            print("I'm close")
            print("Higher")
            min = guess + 1
            max = guess + 5
            five += 1 #proof it passed this before the rest
        elif diff <= 5 and guess > x and five == 0:
            print("I'm close")
            print("Lower")
            min = guess - 5
            max = guess - 1
            five += 1
        elif diff <= 4 and guess < x and five == 1:
            print("I'm closer")
            print("Higher")
            min = guess + 1
            max = guess + 4
            four += 1
        elif diff <= 4 and guess > x and five == 1:
            print("I'm closer")
            print("Lower")
            min = guess - 4
            max = guess - 1
            four += 1
        elif diff <= 3 and guess < x and four == 1:
            print("I'm closer")
            print("Higher")
            min = guess + 1
            max = guess + 3
            three += 1
        elif diff <= 3 and guess > x and four == 1:
            print("I'm closer")
            print("Lower")
            min = guess - 3
            max = guess - 1
            three += 1
        elif diff <= 2 and guess < x and three == 1:
            print("I'm very close")
            print("Higher")
            min = guess + 1
            max = guess + 2
            two += 1
        elif diff <= 2 and guess > x and three == 1:
            print("I'm very close")
            print("Lower")
            min = guess - 2
            max = guess - 1
            two += 1
        elif diff == 1 and guess < x and two == 1:
            print("I'm very close")
            print("Higher")
            min = guess + 1
            max = guess + 1
            two += 1
        elif diff == 1 and guess > x and two == 1:
            print("I'm very close")
            print("Lower")
            min = guess - 1
            max = guess - 1
            two += 1

        #not close
        elif guess < x:
            print("Higher")
            min = guess + 1
        elif guess > x:
            print("Lower")
            max = guess - 1

        #correct
        if guess == x:
            print("Oh yay! I'm right!!")
            break


    again = input("Go again? (yes/no): ")

print("Goobye")
quit()