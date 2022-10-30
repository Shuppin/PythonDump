#- ask the player if they want to be a zombie or a human 
#- generate a random number of zombies 
#- generate a random number of humans 
#- ask the player if they want to (r)un... or (f)ight 
#- if the player chooses to (r)un ... how many zombies chase him/her? 
#- if the player chooses to (f)ight ... 
#- each round - a new (random) number of zombies is added to the existing zombies (cos they convert humans into zombies!) 
#- number of humans should decrease the same number as new zombies 

import random

zombies = random.randint(5,10)
humans = random.randint(5,10)

followZomb = random.randint(1,8)

while True: # Try & Catch for type (string mode) input
    
    try:
        mode = input("Would you like to be a Zombie or Human? ")
        break
    except ValueError:
        print("That is not a valid answer! Please try again")

print("")

if mode.lower().startswith("h"):
    print("You find your self on the run from", zombies, "zombies with", humans, "other humans.")

elif mode.lower().startswith("z"):
    print("You are chasing a group of", humans, "humans with", zombies, "other")

print("")

while True: # Try & Catch for run/hide (string runhide) input
    try:
        runhide = input("Do you wish to run or fight? ")
        break
    except ValueError:
        print("That is not a valid answer! Please try again")

print("")

if mode.lower().startswith("h"):

    if runhide.lower().startswith("r"):

        print("You chose to run...")
        print(followZomb, "zombies notice you as your run away and are now following you.")

        print("")

        while True:
            try:
                print("Do you:")
                print("A) Keep on running in a group")
                print("B) Split up")
                print("C) Stop and fight.")
                rchoice = input("> ")
                break
            except ValueError:
                print("")
                print("Please choose either A, B or C")
                print("")
        
        print("")
            
        if rchoice.lower().startswith("a"):
            print("You choose to run...")
            print("")
            tempRand = random.randint(1,3)
            if tempRand == 1:
                print("The zombies grow tired and stop following you")
                print("Someone says 'Phew! that was a close call!'")
                print("")
            elif tempRand == 2:
                print("The zombies are still following you but you are slowly loosing them")
            elif tempRand == 3:
                print("The zombies are gaining in you and will probably catch up to you")

            print("")

            while True:
                try:
                    print("Do you:")
                    print("A) Keep on running in a group")
                    print("B) Split up")
                    print("C) Stop and fight.")
                    rchoice = input("> ")
                    break
                except ValueError:
                    print("")
                    print("Please choose either A, B or C")
                    print("")

        


    elif runhide.lower().startswith("f"):
        # Not Implemented
        pass 

print("Thanks for playing!")
