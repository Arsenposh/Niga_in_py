def gen(niga):
    for i in range(0, niga + 1):
        yield 2**i
n=int(input()) 
for i in gen(n):
    print(i, end=' ')        