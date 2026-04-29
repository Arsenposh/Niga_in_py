n = int(input())
arr = list(map(int, input().split()))
q = int(input())

for i in range(q):
    parts = input().split()
    op = parts[0]

    if op == "add":
        x = int(parts[1])
        for i in range(n):
            arr[i] = arr[i] + x

    elif op == "multiply":
        x = int(parts[1])
        for i in range(n):
            arr[i] = arr[i] * x

    elif op == "power":
        x = int(parts[1])
        for i in range(n):
            arr[i] = arr[i] ** x

    elif op == "abs":
        for i in range(n):
            if arr[i]<0:
                arr[i] = -arr[i]

print(*arr)
