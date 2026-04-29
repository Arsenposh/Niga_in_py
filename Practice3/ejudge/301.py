n = input()
for i in str(n):
    if int(i)%2 != 0:
        print("Not valid")
        break
else:
    print("Valid")