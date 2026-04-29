n = int(input())
numbers = []
for i in range(n):
    numbers.append(input())

numbers.sort()

count_3 = 0
i = 0

while i < n:
    current = numbers[i]
    count = 1
    i+=1
    while i < n and numbers[i] == current:
        count += 1
        i += 1
    if count == 3:
        count_3 += 1
print(count_3)
