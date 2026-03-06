def generator(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
gen = generator(n)
first = next(gen)
print(first, end='')
for num in gen:
    print(',', num, sep='', end='')