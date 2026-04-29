n = int(input())
numbers = input().split()
for i in range(n):
    numbers[i] = int(numbers[i])

maxn = numbers[0]
minn = numbers[0]
indmax = 0
for i in range(n):
    if numbers[i] > maxn:
        maxn = numbers[i]
        ind = i
for i in range(n):
    if numbers[i] < minn:
        minn = numbers[i]

for i in range(n):
    if numbers[i]!=maxn:
        print(numbers[i], end=' ')
    else:
        print(minn, end=' ')