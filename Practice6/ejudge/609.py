num = int(input())
keys = input().split()
values = input().split()
d = dict(zip(keys, values))
value = input()
if value in d:
    print(d[value])
else:
    print("Not found")