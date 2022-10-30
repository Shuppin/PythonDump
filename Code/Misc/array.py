array = []
while True:
    try:
        array.append(input("Enter a letter you would like add to the list: "))
        break
    except ValueError:
        print("That is not a letter!")
print("Your list now contains", array)