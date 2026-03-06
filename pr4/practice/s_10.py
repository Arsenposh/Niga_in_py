def generator(white, niga):
    for _ in range(niga):
        for item in white:
            yield item

lst = input().split()
n = int(input())

print(*generator(lst, n))
