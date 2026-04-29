line = input().split()
n = int(line[0])
l = int(line[1]) - 1
r = int(line[2])

numbers = input().split()
numbers[l:r] = numbers[l:r][::-1]

for i in numbers:
    print(i, end=' ')
