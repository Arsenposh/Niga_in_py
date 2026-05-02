strr = list(input())
if any(c in "aeiouAEIOU" for c in strr):
    print("Yes")
else:
    print("No")