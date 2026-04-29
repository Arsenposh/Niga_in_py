n = int(input())
numbers = input().split()
for i in range(n):
    numbers[i] = int(numbers[i])

maxn = numbers[0]
ind = 1
for i in range(n):
    if numbers[i] > maxn:
        maxn = numbers[i]
        ind = i + 1

print(ind)
