
#Start

user1 = input("Choose Rock, Paper or Scissors")
user2 = input("Choose Rock, Paper or Scissors")  #Obviously this can't be like this beacause user2 will always know what user1 said first

user1 = user1.lower()
user2 = user2.lower()

final_user1 = "null"
final_user2 = "null"

if user1.startswith("r"):
    final_user1 = "r"

elif user1.startswith("p"):
    final_user1 = "p"

elif user1.startswith("s"):
    final_user1 = "s"


if user2.startswith("r"):
    final_user2 = "r"               

elif user2.startswith("p"):
    final_user2 = "p"

elif user2.startswith("s"):
    final_user2 = "s"


if final_user1 == final_user2:
    print("Its a tie!")

elif final_user1 == "r" and final_user2 == "p":
    print("Player 2 wins!")

elif final_user1 == "r" and final_user2 == "s":
    print("Player 1 wins!")

elif final_user1 == "p" and final_user2 == "r":
    print("Player 1 wins!")

elif final_user1 == "p" and final_user2 == "s":
    print("Player 2 wins!")

elif final_user1 == "s" and final_user2 == "r":
    print("Player 2 wins!")

elif final_user1 == "s" and final_user2 == "p":
    print("Player 1 wins!")


    



#print(final_user1,final_user2) // For testing purposes


