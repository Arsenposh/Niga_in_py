a = int(input())
nums = input().split()
for i in range(a):
    nums[i] = int(nums[i])

for i in range(a):
    for j in range(a-1):
        if nums[j] < nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

for num in nums:
    print(num, end=" ")
