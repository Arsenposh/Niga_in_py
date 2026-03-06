def gen(string):
    for i in range(len(string) - 1, -1, -1):
        yield string[i]

s = input()
print(''.join(gen(s)))
