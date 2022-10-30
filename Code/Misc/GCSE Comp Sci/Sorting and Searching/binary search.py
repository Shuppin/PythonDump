
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def binary_search(nums, query):
    nums = bubble_sort(nums)
    res = _bins(nums, 0, len(nums)-1, query)
    return res

def _bins(nums, low, high, query):

    if high >= low:
 
        mid = (high + low) // 2
        if nums[mid] == query:
            return mid

        elif nums[mid] > query:
            return _bins(nums, low, mid - 1, query)
 
        else:
            return _bins(nums, mid + 1, high, query)
 
    else:
        return -1
 
nums = [4,17,9,12,1,3]
query = 3
 
result = binary_search(nums, query)
print(bubble_sort(nums))

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")