def sq(a):
    for i in range(1, a + 1):
        yield i * i

a=int(input())
for j in sq(a):
    print(j)