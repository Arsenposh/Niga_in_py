# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
print(i)
# Output:  1
#          2
#          4
#          5
#          6

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i) 
# Output:  1
#          3
#          5
#          7
#          9

nums = [1, -1, 2]
i = 0
while i < len(nums):
    if nums[i] < 0:
        i += 1
        continue
    print(nums[i])
    i += 1
# Output:  1
#          2

i = 0
while i < 6:
    i += 1
    if i % 2 == 1:
        continue
    print(i)
# Output: 2
#         4

i = -1
while i < 2:
    i += 1
    if i == 0:
        continue
    print(i)
# Output:  -1
#           1
#           2