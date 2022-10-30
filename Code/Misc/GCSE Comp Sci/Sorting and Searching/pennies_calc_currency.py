currencies = ["GBP", "USD", "JPY"]
exRates = [1, 1.38, 151.46]
symbols = ["£", "$", "¥"]
lowerSymbols = ["p", "c", "bebe yen"]

changeIn = "USD"
index = currencies.index(changeIn)
exRate = exRates[index]
symbol = symbols[index]
lowerSymbol = lowerSymbols[index]


coins = [10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

# Need to make array for different types of notes *sigh*

cost = 0.01*exRate
money = 20*exRate
change = money - cost

change_coins = []

if cost > money:
    print("Not enough money!")

elif cost == money:
    print("No change")

elif money <= 0 or cost <= 0:
    print("Value cannot be below zero!")

else:

    for coin in coins:
        while coin < change:
            change_coins.append(coin)
            change = change - coin       

    print("The cost of the item is", cost)
    print("You have entered", money)

    print("Your change is," , symbol + "{:,.2f}".format(money - cost))

    print("Coins used:")
    for coin in change_coins:
        if coin >= 1:
            print(symbol + str(round(coin, 2)), end=" ")
        else:

            print(str(round(int(coin*100), 2)) + "p", end=" ")
