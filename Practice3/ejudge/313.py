def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

parts = input().split()
primes = []

for i in range(len(parts)):
    num = int(parts[i])
    if is_prime(num):
        primes.append(num)

if primes:
    for p in primes:
        print(p, end=" ")
else:
    print("No primes")