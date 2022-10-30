import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def reader():
    plate = input("Enter you reg: ")

    yearnum = plate[2:4]

    print(yearnum)

    if int(yearnum) < 21:
        print("This car's year is 20" + str(yearnum))
    else:
        print("This car's year is 19" + str(yearnum))

def generator():
    year = int(input("Please enter a year: "))
    loopAmount = int(input("How many number plates would you like? "))

    yearstr = str(year)

    for i in range(loopAmount):
        genPlate = get_random_string(5)
        print( i+1, " |", "Your generated number plate is:", genPlate[:2].upper() + yearstr[2:4], genPlate[2:].upper())

print("Would you like to use:")
print("1) Number plate reader")
print("2) Number plate generator")
choice = int(input("> "))

if choice == 1:
    reader()
elif choice == 2:
    generator()
else:
    print("Not a valid response!")


