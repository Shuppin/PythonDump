def add(x, y):
    return x + y

def subtract(x, y):
    return(x - y)

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def Rdivide(x, y):
    return x // y

def Square(x):
    return x ** 2


print("Select an Operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Rounded Division")
print("6. Square It")

choice = int(input("Enter choice (1/2/3/4/5/6)"))
if choice != (1,6):
    print("Invalid input!")


print("var 'choice' is now", choice)
      
num1 = int(input("Enter first number"))

num2 = int(input("Enter second number"))

if choice == 1:
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == 2:
     print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == 3:
     print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == 4:
     print(num1,"/",num2,"=", divide(num1,num2))

elif choice == 5:
     print(num1,"/",num2,"=", Rdivide(num1,num2))

elif choice == 6:
     print(num1,"Squared is", Square(num1))

else:
    print("Invalid Input")



