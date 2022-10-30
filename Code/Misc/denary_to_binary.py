def x(num):
    if num >= 1:
        x(num//2)
        print(num % 2, end="")
x(int(input("Enter denary number: ")))