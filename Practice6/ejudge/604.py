number = int(input())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
x = zip(nums1, nums2)
sum = 0
for a, b in x:
    sum = sum + a*b
print(sum)