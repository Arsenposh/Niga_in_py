def isUsual(num):
    while num%2 == 0:
        num //= 2
    while num%3 == 0:
        num //= 3
    while num%5 == 0:
        num //= 5
    if num == 1:
        print('Yes')
    else:
        print('No')

num = int(input())
isUsual(num)