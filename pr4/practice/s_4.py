def generator(a, b):
    for i in range(a, b + 1):
        yield i * i
a,b=map(int,input().split())
for j in generator(a, b):
    print(j)