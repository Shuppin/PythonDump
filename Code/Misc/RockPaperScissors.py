import random # Used for random value generation

compchoice=random.choice(["R","P","S"]) # MAke the computer pick rock, paper or scissors


while True:
    print("Pick one of the following")
    print()
    print("(R) Rock")
    print("(P) Paper")
    print("(S) Scissors")
    userchoice=input("Enter R, P or S: ") # Ask the user for their choice

    userchoice = userchoice.upper() # Make the input all upper case

    # This section tells the user what they chose (I don't why i did this i made this in year 7 leave me alone)

    if compchoice == "R":
        print("I selected...Rock")
    elif compchoice == "P":
        print("I selected...Paper")
    else:
        print("I selected...Scissors")
    if userchoice == "R":
        print("You selected...Rock")
        break
    elif userchoice == "P":
        print("You selected...Paper")
        break
    elif userchoice == "S":
        print("You selected...Scissors")
        break
    else:
        print("Incorrect selection")

# This section determines if you won or not

if compchoice == "R":
    if userchoice == "R":
        print("It is a draw")
    elif userchoice == "P":
        print("Paper wraps rock, you win")
    else:
        print("Rock blunts scissors, I win")
if compchoice == "P":
    if userchoice == "R":
        print("Paper wraps rock, I win")
    elif userchoice == "P":
        print("It is a draw")
    else:
        print("Scissors cuts paper, you win")
if compchoice == "S":
    if userchoice == "R":
        print("Rock blunts scissors, I win")
    elif userchoice == "P":
        print("Scissors cuts paper, I win")
    else:
        print("It is a draw")
