print("All drinks are 80p with free milk and sugar")

menu = ["tea", "coffee"]
extras = ["no extra", "milk", "sugar"]
money = 0

print("Please pick a drink: ")
for i, item in enumerate(menu):
    print(str(i+1) + ") " + item)

drink = int(input("> "))

print("Please pick an extra: ")
for i, item in enumerate(extras):
    print(str(i+1) + ") " + item)

extra = int(input("> "))

print("Your order is [" + menu[drink-1] + "," + extras[extra-1] + "]")

print("That will be £0.80")

while True:
    print("Please enter money (£)")
    money += float(input("> "))

    if money < 0.8:
        print("That is not enough!")
        print("Current change:", money)
        change = 0

    elif money > 0.8:
        change = money - 0.8
        break

    else:
        change = 0
        break

if change != 0:

    currency = "£{:,.2f}".format(change)

    print("Your change is", currency)

print("Enjoy your drink!")