from random import randint # random module inport used for dice rolls

# Dice Program

## Variable Assignment

p1_score = 0
p2_score = 0

p1_name = input("Enter player 1 name:\n")
p2_name = input("Enter player 2 name:\n")

## Line Break

print("--------------------")

## Game

for i in range(5): # 5 rounds

    ### Generate dice ints
    p1 = [randint(1,6), randint(1,6)]
    p2 = [randint(1,6), randint(1,6)]
    ### Add another dice roll if the first two rolls are equal
    if p1[0] == p1[1]:
        p1[1] += randint(1,6)
    if p2[0] == p2[1]:
        p2[1] += randint(1,6)
    ### Check if score is odd or even
    if (sum(p1) % 2) == 0: #### Is even
        p1_score += 10
    else: #### Is odd
        p1_score -= 5
    ### Same for player two
    if (sum(p2) % 2) == 0:
        p2_score += 10
    else:
        p2_score -= 5
    ### Make sure player score doesn't go below 0
    if p1_score < 0:
        p1_score = 0
    if p2_score < 0:
        p2_score = 0

## Checking win condition

if p1_score > p2_score:
    print(f"{p1_name} wins by {p1_score-p2_score} points!")
elif p2_score > p1_score:
    print(f"{p2_name} wins by {p2_score-p1_score} points!")

### If score is equal then run a sudden death subroutine

else:  
    while True:
        p1_score += randint(1,6)
        p2_score += randint(1,6)
        if p1_score > p2_score:
            print(f"{p1_name} wins by {p1_score-p2_score} points!")
            break
        if p1_score < p2_score:
            print(f"{p2_name} wins by {p2_score-p1_score} points!")
            break

## Show final score

print(f"--------------------\n{p1_name}: {p1_score} points\n{p2_name}: {p2_score} points")