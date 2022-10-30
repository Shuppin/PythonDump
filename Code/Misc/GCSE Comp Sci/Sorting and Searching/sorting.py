import time
import random

def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def help(names):
    print("Welcome to sorting.py")

    while True:
        print("|----------------------------------------------|")
        print("| Select one of the following to find out more |")
        print("|                                              |")
        for i, name in enumerate(names):
            if name != names[-1]:
                print(f"| {i+1}) {name}", end="")
                print(" "*(42-len(name)) + "|")
            else:
                print(f"| {i+1}) Exit", end="")
                print(" "*(38) + "|")

        print("|                                              |")
        print("|----------------------------------------------|")
        
        while True:
            try:
                choice = int(input("> "))
                if 0 < choice < len(names)+1:
                    break
                else:
                    print("Invalid input!")
            except ValueError:
                print("Invalid input!")

        print(choice)
        if choice == len(names):
            break
        if choice == 1:
            print("Bubble sort.")
            print("Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.")
            print("This is one of the slowest of all the sorting algorithms but is easy to implement")



def insertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1
        while j >= 0 and key < nums[j] :
                nums[j + 1] = nums[j]
                j -= 1
        nums[j + 1] = key
    return nums

def selectionSort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j     
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


######################################################### Quick Sort code
def quickStartInitiator(nums):
    _qs(0, len(nums) - 1, nums)

# Partition & QuickSort code by Adnan Aliakbar
def partition(start, end, nums):
    pivot_index = start 
    pivot = nums[pivot_index]
    while start < end:
        while start < len(nums) and nums[start] <= pivot:
            start += 1
        while nums[end] > pivot:
            end -= 1
        if(start < end):
            nums[start], nums[end] = nums[end], nums[start]
    nums[end], nums[pivot_index] = nums[pivot_index], nums[end]
    return end
def _qs(start, end, nums): # Internal recursive quick sort function
    if (start < end):
        p = partition(start, end, nums)
        _qs(start, p - 1, nums)
        _qs(p + 1, end, nums)
#########################################################################

names = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Quick Sort", "Help!!"]
sorts = ["bubbleSort", "insertionSort", "selectionSort", "quickStartInitiator"]

nums = []

AMOUNT = 10000

for i in range(AMOUNT):
    nums.append(random.randint(0,1000))

print("Please select a sorting algorithm to run")
for i, name in enumerate(names):
    print(f"{i+1})", name)

while True:
    try:
        choice = int(input("> "))
        if 0 < choice < len(names)+1:
            break
    except ValueError:
        print("Invalid input!")

if names[choice-1] == names[-1]:
    help(names)

else:
    start = time.time()

    exec("nums = " + sorts[choice-1] + "(" + str(nums) + ")")

    end = time.time()

    elapsed = end - start

    if len(str((elapsed*1000))) > 7:
        print(sorts[choice-1]+ "() took " + str(round(elapsed, 3)) + "s with", AMOUNT, "values." )

    else:
        print(sorts[choice-1]+ "() took " + str(round(elapsed*1000, 3)) + "ms with", AMOUNT, "values." )


