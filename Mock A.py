def misc(aes, m2, m3):
    maths = (m2 + m3)/2
    if aes < 60:
        return("Sorry, you did not progress because you must score at least 60 in Term 3 in AES")
    elif maths < 65:
        return("Sorry, you did not progress because your Maths 2 and Maths 3 average is less than 65")
    else:
        return("WOOP WOOP! CONGRATULATIONS, YOU PROGRESSED!")

#Term 1 input
while True:
    print("# # # Term 1 # # #")
    try:
        AES1 = int(input("AES: "))
        Maths1 = int(input("Maths 1: "))
        Physics1 = int(input("Physics 1: "))
        Comp = int(input("Computer Programming 1: "))
        if AES1 < 0 or AES1 > 100 or Maths1 < 0 or Maths1 > 100 or Physics1 < 0 or Physics1 > 100 or Comp < 0 or Comp > 100:
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
        Chem = int(input("Chemistry 1: "))
        Maths2 = int(input("Maths 2: "))
        Physics2 = int(input("Physics 2: "))
        if AES2 < 0 or AES2 > 100 or Maths2 < 0 or Maths2 > 100 or Physics2 < 0 or Physics2 > 100 or Chem < 0 or Chem > 100:
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
        Physics3 = int(input("Physics 3: "))
        Design = int(input("Creative Design: "))
        if AES3 < 0 or AES3 > 100 or Maths3 < 0 or Maths3 > 100 or Physics3 < 0 or Physics3 > 100 or Design < 0 or Design > 100:
            print("That is not a valid input.")
        else:
            print("Thank you, Term 3 is inputted.")
            break
    except:
        print("That is not a number")

#Analysis
overall = (AES1 + Maths1 + Physics1 + Comp + AES2 + Chem + Maths2 + Physics2 + AES3 + Maths3 + Physics3 + Design)/12
if AES1 < 40:
    print("Sorry, you did not progress because you must score at least 40 in Term 1 in AES")
elif Maths1 < 40:
    print("Sorry, you did not progress because you must score at least 40 in Maths 1")
elif Physics1 < 40:
    print("Sorry, you did not progress because you must score at least 40 in Physics 1")
elif Comp < 40:
    print("Sorry, you did not progress because you must score at least 40 in Computer Programming")
elif AES2 < 40:
    print("Sorry, you did not progress because you must score at least 40 in Term 2 in AES")
elif Chem < 40:
    print("Sorry, you did not progress because you must score at least 40 in Chemistry")
elif Physics2 < 40:
    print("Sorry, you did not progress because you must score at least 40 in Physics 2")
elif Physics3 < 40:
    print("Sorry, you did not progress because you must score at least 40 in Physics 3")
elif Design < 40:
    print("Sorry, you did not progress because you must score at least 40 in Creative Design")
elif overall < 60:
    print("Sorry, you did not progress because you must score an average of 60% overall")
else:
    print(misc(AES3, Maths2, Maths3))

quit()