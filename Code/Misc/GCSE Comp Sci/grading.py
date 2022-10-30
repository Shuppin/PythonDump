while True:
    try:
        gradeIn = int(input("Please enter your standardised grade: "))
        if gradeIn < 0:
            print("Grade must be a positive number!")
        else:
            break
    except ValueError:
        print("Not a valid response!")
    except:
        print("An unkown error occured, Please try again")

if gradeIn < 50:
    print("You are a grade 1")
elif 66 > gradeIn > 49:
    print("You are a grade 2")
elif 71 > gradeIn  > 65:
    print("You are a grade 3")

# And so on...

elif gradeIn > 124:
    print("You are a grade 9")
else:
    print("Number invalid")
