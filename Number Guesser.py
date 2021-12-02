import random
again = "yes"

while again == "yes":
    min = 1
    max = 100
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

        if diff <= 5 and guess < x:
            print("I'm close")
            print("Higher")
            min = guess + 1
            max = guess + 5
        elif diff <= 5 and guess > x:
            print("I'm close")
            print("Lower")
            min = guess - 5
            max = guess - 1
        elif guess < x:
            print("Higher")
            min = guess + 1
        elif guess > x:
            print("Lower")
            max = guess - 1
        if guess == x:
            print("Oh yay! I'm right!!")
            break


    again = input("Go again? (yes/no): ")

print("Goobye")
quit()