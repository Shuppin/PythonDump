def TempConv(x=None):
    if x is not None:
        x=x*1.8
        x=x+32
        return x

def PoundToEuro(x=None):
    if x is not None:
        x=x*1.12
        return x

def EuroToPound(x=None):
    if x is not None:
        x=x*0.89
        return x

while True:
    while True:
        try:
            print("")
            print("| Function    | ID |")
            print("|-------------|----|")
            print("| TempConv    | 01 |")
            print("| PoundToEuro | 02 |")
            print("| EuroToPound | 03 |")
            print("|-------------|----|")
            print("")
            print("Enter an function id:")
            tempIn = input("> ")
            break
        except ValueError:
            print("Not a valid response!")

    tempIn = tempIn.replace("0", "")

    if tempIn == "1":
        temp = TempConv(int(input("Enter the the tempurature you would like to convert to fahrenheit: ")))
        print(temp)
        break
    elif tempIn == "2":
        temp = PoundToEuro(int(input("Enter the value you would like to convert: ")))
        print(temp)
        break
    elif tempIn == "3":
        temp = EuroToPound(int(input("Enter the value you would like to convert: ")))
        print(temp)
        break
    else:
        print("Not a valid response!")

