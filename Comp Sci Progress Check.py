#Term 1 input
while True:
    print("# # # Term 1 # # #")
    try:
        AES1 = int(input("AES: "))
        Maths1 = int(input("Maths 1: "))
        Physics1 = int(input("Physics 1: "))
        Comp1 = int(input("Computer Programming 1: "))
        if AES1 < 0 or AES1 > 100 or Maths1 < 0 or Maths1 > 100 or Physics1 < 0 or Physics1 > 100 or Comp1 < 0 or Comp1 > 100:
            print("That is not a valid input.")
        else:
            print("Thank you, Term 1 is inputted.")
            break
    except:
        print("That is not a number")

#Term 2 input
while True:
    print("# # # Term 2 # # #")
    try:
        AES2 = int(input("AES: "))
        Maths2 = int(input("Maths 2: "))
        Comp2 = int(input("Computer Programming 2: "))
        SE = int(input("Software Engineering: "))
        if AES2 < 0 or AES2 > 100 or Maths2 < 0 or Maths2 > 100 or SE < 0 or SE > 100 or Comp2 < 0 or Comp2 > 100:
            print("That is not a valid input.")
        else:
            print("Thank you, Term 2 is inputted.")
            break
    except:
        print("That is not a number")

#Term 3 input
while True:
    print("# # # Term 3 # # #")
    try:
        AES3 = int(input("AES: "))
        Maths3 = int(input("Maths 3: "))
        Alg = int(input("Algorithms: "))
        Design = int(input("Creative Design: "))
        if AES3 < 0 or AES3 > 100 or Maths3 < 0 or Maths3 > 100 or Alg < 0 or Alg > 100 or Design < 0 or Design > 100:
            print("That is not a valid input.")
        else:
            print("Thank you, Term 3 is inputted.")
            break
    except:
        print("That is not a number")

#Analysis
overall = (AES1 + Maths1 + Physics1 + Comp1 + AES2 + Comp2 + Maths2 + SE + AES3 + Maths3 + Alg + Design)/12
if AES1 < 40:
    print("Sorry, you did not progress because you must score at least 40 in Term 1 in AES")
elif Maths1 < 40:
    print("Sorry, you did not progress because you must score at least 40 in Maths 1")
elif Physics1 < 40:
    print("Sorry, you did not progress because you must score at least 40 in Physics 1")
elif Comp1 < 40:
    print("Sorry, you did not progress because you must score at least 40 in Computer Programming 1")
elif AES2 < 40:
    print("Sorry, you did not progress because you must score at least 40 in Term 2 in AES")
elif Maths2 < 60:
    print("Sorry, you did not progress because you must score at least 60 in Maths 2")
elif Comp2 < 40:
    print("Sorry, you did not progress because you must score at least 40 in Computer Programming 2")
elif SE < 40:
    print("Sorry, you did not progress because you must score at least 40 in Software Engineering")
elif AES3 < 60:
    print("Sorry, you did not progress because you must score at least 60 in Term 3 in AES")
elif Maths3 < 40:
    print("Sorry you did not progress because you must score at least 40 in Maths 3")
elif Alg < 40:
    print("Sorry, you did not progress because you must score at least 40 in Algorithms")
elif Design < 40:
    print("Sorry, you did not progress because you must score at least 40 in Creative Design")
elif overall < 60:
    print("Sorry, you did not progress because you must score an average of 60% overall")

quit()
