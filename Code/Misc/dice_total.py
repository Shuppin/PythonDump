import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

def roll():
    print("Initiating roll()")
    dice1 = random.randint(1,6)
    print("dice 1 is", dice1)
    dice2 = random.randint(1,6)
    print("dice 2 is", dice2)

while True:
    if dice1 + dice2 == 7 or dice1 + dice2 == 11:
        print("Congrats you win! You rolled ", dice1 + dice2)
        break
    elif dice1 + dice2 == 2 or dice1 + dice2 == 3 or dice1 + dice2 == 12:
        print("You lose :( - You rolled ", dice1 + dice2)
        break
    else:
        print("You rolled ", dice1 + dice2)
        print("You didn't roll a correct number, Rolling again...")
        roll()