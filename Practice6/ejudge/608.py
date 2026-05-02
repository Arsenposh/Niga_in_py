num = input()
nums = list(map(int, input().split()))
set_s = set(nums)
sorted_s = sorted(set_s)
for s in sorted_s:
    print(s, end=" ")