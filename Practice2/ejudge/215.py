n = int(input())
surnames = []

for i in range(n):
    surnames.append(input())

surnames.sort()

count = 1 
for i in range(1, n):
    if surnames[i] != surnames[i-1]:
        count += 1

print(count)
