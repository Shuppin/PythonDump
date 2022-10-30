while True:
    while True:
        while True:
            print("Select an Operation")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Integer Division")
            print("6. Square It")
            try:
                choice = int(input())
                break
            except ValueError:
                print("Invalid choice, please try again")

        if 0 < choice < 7:
            break
        else:
            print("Invalid input!")
            print("Please Try Again")

    if choice == 1:
        answer = int(input("Enter your first number: ")) + int(input("Enter your second number: "))
    elif choice == 2:
        answer = int(input("Enter your first number: ")) - int(input("Enter your second number: "))
    elif choice == 3:
        answer = int(input("Enter your first number: ")) * int(input("Enter your second number: "))
    elif choice == 4:
        answer = int(input("Enter your first number: ")) / int(input("Enter your second number: "))
    elif choice == 5:
        answer = int(input("Enter your first number: ")) // int(input("Enter your second number: "))
    elif choice == 6:
        answer = int(input("Enter your first number: ")) ** int(input("Enter your power: "))

    print("Your answer is", answer)

    loop = input("Would you like to perform another calculation?")

    if loop.lower().startswith("n"):
        break
    elif loop.lower().startswith("y"):
        pass
    else:
        pass
