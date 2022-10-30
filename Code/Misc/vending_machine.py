# Vending Machine Simulation
# Made by [Removed] [Removed]

import locale
locale.setlocale( locale.LC_ALL, '' )

machine = ["Mars Bar", "Twix", "Rats", "Milky Way", "Coca Cola"]
prices = ["£1.99", "£29.99", "£328.99", "£2900000000.00", "£80380000000000.00"]
stockLengths = [8, 4, 4, 9, 9]
priceLengths = [5, 6, 7, 14, 18]
slot = 0

slot_input = 0
maxStockLength = 0
maxPriceLength = 0
state = "nul"

#null = "null"

def load():

    # Other Variables

    global slot_input
    global maxStockLength
    global maxPriceLength
    global state

    slot_input = 0
    maxStockLength = 0
    maxPriceLength = 0
    state = "nul"

    # Arrays

    global machine
    global prices
    global stockLengths
    global priceLengths

    machine = []
    prices = []
    stockLengths = []
    priceLengths = []

    while True: # Try & Catch ValueError for number of slots input
        try:
            slot_input = int(input("How many items would you like to put in the vending machine? "))
            if slot_input < 1: # Make sure the value inputted is above 0 
                print("Please make sure your value is higher than or equal to 1")
            else:
                break
        except ValueError:
            print("That is not a valid value! Please try again.")
    slot = slot_input
    slot_input = slot
    while slot > 0: # Vending machine loading system
        while True: # Try & Catch ValueError for stock input
            try:
                print("Enter an item to fill up slot", slot)
                stock = input("> ")
                stock = stock.lower().capitalize()  # Make the inputted value lowercase then re-capitalise it to make it look nice
                stockLength = len(stock) # Get the length of input 'stock'
                stockLengths.append(stockLength)
                machine.append(stock)     
                break
            except ValueError:
                print("That is not a valid item! Please try again.")

        while True:
            try:
                price = float(input("Enter the price for your item (£): "))
                rprice = locale.currency(price)
                priceLength = len(str(rprice))
                priceLengths.append(priceLength)
                break
            except ValueError:
                    print("That is not a valid price! Please try again.")

        prices.append(rprice)

        maxStockLength = max(stockLengths)
        maxPriceLength = max(priceLengths)
        
        slot = slot - 1
        print("Succesfully put", stock , "in the machine and set the price to" , str(rprice))

    print("The vending machine is now full!")
    print("Your vending machine contains: ")
    print(', '.join(machine))

    print("Entering user mode...")

    state = "load"
    user()


def user():

    if state == "user":
        maxStockLength = 9
        maxPriceLength = 18
        slot_input = 5



    BstockSpaces = (maxStockLength - 3)
    BpriceSpaces = (maxPriceLength - 4)
    BstockSpacesAmount = " " * BstockSpaces
    CstockSpacesAmount = "-" * BstockSpaces
    BpriceSpacesAmount = " " * BpriceSpaces
    CpriceSpacesAmount = "-" * BpriceSpaces
    print("Item" + BstockSpacesAmount + "| Price" + BpriceSpacesAmount + "| Item ID")
    print("----" + CstockSpacesAmount + "|------" +  CpriceSpacesAmount + "|--------")
    for x in range (slot_input): # Displays list
        stockSpaces = (maxStockLength - stockLengths[x]) + 1
        priceSpaces = (maxPriceLength - priceLengths[x]) + 1
        stockSpacesAmount = " " * stockSpaces
        priceSpacesAmount = " " * priceSpaces
        print(machine[x] + stockSpacesAmount + "|", str(prices[x]) + priceSpacesAmount + "|", x+1)
    print("")
    
    print("Enter the item ID of what you would like to buy: ")
    item = int(input("> "))


#print("Would you like to stock the vending machine or use it?")

#print("Enjoy!")

mode = input("Would you like to stock up the machine or use the machine?")
mode = mode.lower()

null = "null"

if mode.startswith("lo"):
    print("Entering loading mode...")
    state = "load"
    load()

elif mode.startswith("stoc"):
    print("Entering loading mode...")
    state = "load"
    load()

elif mode.startswith("us"):
    print("Entering user mode...")
    state = "user"
    user()
