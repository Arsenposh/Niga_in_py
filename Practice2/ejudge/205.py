a = int(input())
while a > 1:
    if a % 2 != 0:
        print("NO")
        break
    else:
        a = a // 2
else:
    print("YES")
