n = int(input())
numbers = input().split()
for i in range(n):
    numbers[i] = int(numbers[i])

maxn = numbers[0]
for i in range(1, n):
    if numbers[i] > maxn:
        maxn = numbers[i]
print(maxn)
