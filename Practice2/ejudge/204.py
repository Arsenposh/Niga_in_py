n = int(input())
count = 0
numbers = input().split()
for i in numbers:
    if int(i) > 0:
        count += 1
print(count)
