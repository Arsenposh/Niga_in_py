def generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = int(input())
gen = generator(n)
first = next(gen, None)
if first is not None:
    print(first, end='')
    for num in gen:
        print(',', num, sep='', end='')