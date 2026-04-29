a = int(input())
numbers = input().split()
for i in range(a):
    numbers[i] = int(numbers[i])

for i in numbers:
    print(i**2, end=' ')