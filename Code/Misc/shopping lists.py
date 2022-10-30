#OMG this program works beautifully!!!

shoppingA = ["apples", "bread", "chocolate", "dried apricot"]
shoppingB = ["shoes" , "hat", "tie", "socks"]



shopping = shoppingA

list1 = True

while list1 == True:

    showlist = False
    


    print("1. Add an item to your shopping list")
    print("2. Add multiple items to your shopping list")
    print("3. Add an item to a specific place in the list")
    print("4. Remove an item")
    print("5. Show list")
    print("6. Remove all items from your list")
    print("7. Change lists")
    choice = int(input("Which action would you like to peform? "))




    if choice == 1:
        addlist = input("What would you like to add to your shopping list? ")
        if addlist in shopping:
            print("This item is already on your list")
            showlist = False
            

        else:
            shopping.append(addlist)
            print("Done!")
            showlist = True
                   

    elif choice == 2:
        addmultiplelist = input("What would you like to add to your shopping list? ")
        addmultiplelistA = input("What other item would you like to add to your shopping list? ")
        addmultiplelistB = input("What other item would you like to add to your shopping list? ")
        shopping.extend([addmultiplelist, addmultiplelistA, addmultiplelistB])
        print("Done!")
        showlist = True

    elif choice == 3:
        customadd = input("Which item would you like to add? ")
        customnom = int(input("In what place 1,2,3,etc..? "))
        shopping.insert(customnom - 1,customadd)
        print("Done!")
        showlist = True

    elif choice == 4:
        removeitem = input("Which item would you like to remove? ")
        shopping.remove(removeitem)
        showlist = True

    elif choice == 5:
        print(shopping)
        showlist = False

    elif choice == 6:
        shopping.clear()
        print("Done!")
        showlist = True

    elif choice == 7:
        if shopping == shoppingA:
            shopping = shoppingB
            print("Swaped to list 2")

        else:
            shopping = shoppingA
            print("Swaped to list 1")

    else:
        print("Invalid choice")


    if showlist == True:
        print("Your shopping updated list")
        print(shopping)

    

    endloop = True

    while endloop == True:
        
        another = input("Would you like to peform another action?(Y/N) ")

        another = another.lower()
       

        if another.startswith("y"):
            list1 = True
            endloop = False

        elif another.startswith("n"):
            list1 = False
            endloop = False


        else:
            print("Invalid input")
            list1 = False
            endloop = True

    




