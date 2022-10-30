# Variable declaration

items = ["Margherita", "Pepperoni", "Hawaiian", "Buffalo Chicken", "Vegetable Feast"] # Possible items you can order
prices = [3.55, 3.99, 4.35, 4.59, 3.99] # And their prices corresponding to index

price = 0
order = []

def add_pizza(price, *args): # Gets called when the user wants to add a pizza to the order

    for i, item in enumerate(items): # Print all items in list 'items' with number indexes
        print(str(i+1) + ")", item)

    while True: # Main function loop
        while True: # Valid input check loop
            try:
                choice = int(input("Which pizza would you like? "))
                pizza = items[choice-1]
                order.append(pizza)
                price += prices[choice-1]
                break
            except:
                print("Invalid value! >:(")
        while True: # Add to order loop
            try:
                loop = input("Would you like to order another pizza? (Y/N) ")
                break
            except ValueError:
                print("Invalid value! >:(")
        
        if loop.lower().startswith("n"): # If the user doesn't want another pizza, continue
            break

        elif loop.lower().startswith("y"): # If they do, loop back to the start
            pass

        else: # Invalid input! >:(
            print("Invalid input! >:(")
            break

    return price

price = add_pizza(price) # Initial call of main function to start program
while True: # Correct order check loop

    for item in items:
        oc = order.count(item)
        if oc == 1:
            print("1", item, "pizza")
        elif oc > 0:
            print(oc, item, "pizzas")

    print("Is this order correct? (Y/N)")
    correct = input("> ")
    if correct.lower().startswith("y"):
        break
    elif correct.lower().startswith("n"):
        price = add_pizza(price)
    else:
        print("Invalid input! >:(")

print("That will be £" + str(price)) # Print price



