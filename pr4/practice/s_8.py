def gen(niga):
    for i in range(2, niga + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i
n=int(input())
for i in gen(n):
    print(i, end=' ')