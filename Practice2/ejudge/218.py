n = int(input())
strings = []

for i in range(n):
    strings.append(input())

another = []
for string in strings:
    if string not in another:
        another.append(string)
another.sort()

for string in another:
    for i in range(n):
        if strings[i] == string:
            print(f"{string} {i+1}")
            break

