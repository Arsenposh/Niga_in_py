a = int(input())
numbers = input().split()
for i in range(a):
    numbers[i] = int(numbers[i])

another = []
for num in numbers:
    if num not in another:
        print("YES")
        another.append(num)
    else:
        print("NO")