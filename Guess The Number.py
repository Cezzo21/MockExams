import random
again = "yes"

while again == "yes":
    print("--- G U E S S   T H E   N U M B E R ---")
    #range
    print("Pick my range")
    while True:
        try:
            min = int(input("from: "))
            max = int(input("to: "))
            x = random.randint(min, max)
            break
        except:
            print("I need integers (in increasing order).")
    while True:
        while True:
            try:
                guess = int(input("Guess (from " + str(min) + " to " + str(max) + "): "))
                break
            except:
                print("bro it's an integer")
        #difference (to see if you're close)
        if x < guess:
            diff = guess - x
        elif x > guess:
            diff = x - guess
        elif x == guess:
            diff = 10 #this is obviously false, I just don't want the bot to print "close" if it's correct, so I tricked it :)
        if diff <= 3:
            print("You're close")
        #answers
        if guess > max or guess < min:
            print("bro, that's not even in the range you picked")
        elif guess == x:
            print("Correct!")
            break
        elif guess < x:
            print("Higher")
        elif guess > x:
            print("Lower")
    #go again
    again = str(input("Go again? (yes/no): "))

#quit
print("Goodbye")
quit()