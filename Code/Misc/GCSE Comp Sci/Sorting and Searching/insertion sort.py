# Wiki ref
# i ← 1
# while i < length(A)
#     j ← i
#     while j > 0 and A[j-1] > A[j]
#         swap A[j] and A[j-1]
#         j ← j - 1
#     end while
#     i ← i + 1
# end while


nums = [1, 17, 4, 3, 9, 20, 11]

for i, num in enumerate(nums):
    x = i-1
    while num < nums[x] and x >= 0:
        nums[x+1] = nums[x]
        x -= 1
    nums[x+1] = num
