import random

distance = 230
counter = 0
CLUB = random.randint(1, 3)

def hit(distance):
    for i in range(CLUB):
        hit_strength = random.choices(list(range(10,231,10)), weights=(32, 16, 16, 8, 8, 8, 8, 6, 6, 6, 6, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 1), k=1)
    hit_strength = hit_strength[0]
    if hit_strength <= 15:
        hit_strength = 0
        print("Miss!")
    else:
        print("Hit with a strength of", hit_strength)
    distance -= hit_strength
    return distance

while distance > -1:
    distance = hit(distance)
    counter += 1
    print(distance)

counter = 0
if counter == 1:
    print("Hole in one!")
elif counter == 2:
    print("Eagle!")
elif counter == 3:
    print("Birdie!")
elif counter == 4:
    print("Par")