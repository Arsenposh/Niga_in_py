chislo = input()
nums = list(map(int, input().split()))
if all(n >= 0 for n in nums):
    print('Yes')
else:
    print("No")