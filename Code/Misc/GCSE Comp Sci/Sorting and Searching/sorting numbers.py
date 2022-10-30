
numbers = [47, 34, 1029, 3, 94, 64, 9]

def BubbleSort(numbers):
    sureGoodOrder = False
    #swaps = 1
    counter = 1
    
    #while swaps > 0:
    while sureGoodOrder == False :
        #swaps = 0
        sureGoodOrder = True
        print()
        print("** Start of list, assuming a good order, fingers crossed **")
        
        for i in range(len(numbers)-1):
            print(counter,"-->", numbers, "   testing:",numbers[i],numbers[i+1])
            counter = counter + 1

            if numbers[i] > numbers [i + 1]: #bubble test
                
                #swaps = swaps + 1 #swaps gonna happen
                sureGoodOrder = False

                bigger = numbers[i] #swap storage
                smaller = numbers [i + 1]

                print("      Bad Order. SWAPING:", bigger, smaller)
                numbers[i] = smaller #swap happening...
                numbers[i+1] = bigger

    print("Yes, Good Order finally found! Final order", numbers)
    print("Number of comparisons ",counter - 1)

BubbleSort(numbers)
    

                            
