
def median_m(data):
    n = len(data)
    if n == 0:
        return None
    if n % 2 == 1:
        return data[n // 2]
    else:
        i = n // 2
        return (data[i - 1] + data[i]) / 2

nums = []

print("Enter 'done' once you have entered all your numbers")

while True:
    num = input("Enter your num: ")
    if num == 'done':
        break
    try:
        num = int(num)
        nums.append(num)
    except ValueError:
        print("Invalid input")
    
nums.sort()

ave = sum(nums)/len(nums)

n = len(nums)
if n % 2 == 1:
    median = nums[n // 2]
else:
    i = n // 2
    median = (nums[i - 1] + nums[i]) / 2

min_num = min(nums)

max_num = max(nums)

range = max(nums) - min(nums)

#print(ave, median, min_num, max_num, range)

print(median)