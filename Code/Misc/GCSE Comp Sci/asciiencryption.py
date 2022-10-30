def encrypt():
    while True:
        try:
            print("Enter a word you would liek to encrypt")
            tempIn = input("> ")
            break
        except ValueError:
            print("Not a valid response!")
    
    terms = []

    for i in range(len(tempIn)):
        asciicode = ord(tempIn[i])
        terms.append(str(asciicode))

    