num = input()
lis = list(map(str, input().split()))
max_s = max(lis, key=len)
print(max_s)