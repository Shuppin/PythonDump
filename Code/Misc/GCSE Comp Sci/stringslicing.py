while True:
    try:
        print("Enter a word")
        tempIn = input("> ")
        break
    except ValueError:
        print("Not a valid response!")

terms = []

for i in range(len(tempIn)):
    asciicode = ord(tempIn[i])
    terms.append(str(asciicode))

print(tempIn, terms)



