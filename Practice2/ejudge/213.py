import math
a = int(input())
isPrime = True
lim = int(math.sqrt(a))

for i in range(2, lim):
    if a%i==0:
        isPrime = False
        break
    else:
        isPrime = True
print("Yes") if isPrime else print("No")