#import math for GCD
import math
#Quit variable
Quit = "n"
#Loop until quit = yes
while Quit == "n":
    #loop the question until a valid input is given
    while True:
        try:
            print("# # # Tell me where your line crosses the X and Y axis. Values must be integers. # # #")
            A = int(input("Where does your line cross the X-axis? "))
            B = int(input("Where does your line cross the Y-axis? "))
            if A == 0 and B == 0:
                print("Sorry, I need two points.")
            elif A == 0 and not B == 0:
                print("That is just the Y-axis i.e. x=0")
                print("Give me non-zero integers please :)")
            elif B == 0 and not A == 0:
                print("That is just the X-axis i.e. y=0")
                print("Give me non-zero integers please :)")
            else:
                print("Thank you. I will find the equation of the line.")
                break
        except:
            print("Sorry, that is not a number")
    #calculate C
    C = A*B
    #consider GCD
    GCD = math.gcd(A, B, C)
    A /= GCD
    B /= GCD
    C /= GCD
    #you want C to be positive for some reason???y
    if B < 0:
        A *= -1
        B *= -1
        C *= -1
    #print the line and clean it
    print(("Line: " + str(int(B)) + "x" + "+" + str(int(A)) + "y=" + str(int(C))).replace("-1","-").replace("1x","x").replace("1y","y").replace("+-", "-"))
    #ask to quit
    Quit = str(input("Quit? y/n "))
    if Quit == "y":
        print ("Goodbye")
        break
quit()
