number = int(input())
strr = list(map(str, input().split()))
x = enumerate(strr)
for word, i in x:
    print(f"{word}: {i}", end=" ")