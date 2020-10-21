import random

lowerBound = 0
upperBound = 0
while lowerBound >= upperBound:
    lowerBound = int(input("Please enter an integer lower bound: "))
    upperBound = int(input("Please enter an integer uppper bound: "))
    if lowerBound >= upperBound:
        print("Your lower bound is greater than or equal to your lower bound, please try again")
random.seed()
randNum = random.randrange(lowerBound, upperBound)
print(f"A random integer between {lowerBound} (inclusive) and {upperBound} (exclusive) has been generated")
userNum = 0
while userNum != randNum:
    userNum = int(input("Please input an integer guess: "))
    if userNum < randNum:
        print(f"Your input, {userNum}, is too small, please try again")
    elif userNum > randNum: 
        print(f"Your input, {userNum}, is too large, please try again")
    else:
        print(f"Congratulations, your input {userNum}, is correct")
