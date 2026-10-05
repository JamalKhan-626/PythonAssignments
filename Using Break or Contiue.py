while True:
    x = (input("Please Enter your number here: "))
    if x.isdigit():
        x = int(x)
        break
    else:
        print("Please Enter an integer: ")

if (97<= x <=100):
        print(" Grade is A+")

elif (93<= x <=96):
        print(" Grade is A")

elif (90<= x<=92):
        print(" Grade is A-")

elif (87<= x<=89):
        print(" Grade is B+")

elif (83<= x<=86):
        print(" Grade is B")

else:
         print("no grade is assigned")