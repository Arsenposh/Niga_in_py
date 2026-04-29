n = int(input())
numbers = input().split()
for i in range(n):
    numbers[i] = int(numbers[i])

maxCount = 0
mostFrequent = numbers[0]

for i in range(n):
    count = 0
    for j in range(n):
        if numbers[j] == numbers[i]:
            count += 1
    if count > maxCount:
        maxCount = count
        mostFrequent = numbers[i]
    elif count == maxCount:
        mostFrequent = min(mostFrequent, numbers[i])

print(mostFrequent)
