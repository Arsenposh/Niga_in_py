number = int(input())
num= list(map(int, input().split()))

def fil(n):
    if n%2==0:
        return True
    else:
        return False

even = list(filter(fil, num))
print(len(even))
    