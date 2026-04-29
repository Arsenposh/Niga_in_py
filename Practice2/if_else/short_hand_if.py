#Short Hand If statement
a = 33
b = 200
if a < b: print("a is less than b")

c = 67
if c > 50: print("c is greater than 50")


#Short Hand If...Else statement
a = 33
b = 200
print("A") if a > b else print("B")
# Output: B

#You can also have multiple else statements on the same line
a = 33
b = 33
print("A") if a > b else print("=") if a == b else print("B")


c = 200
d = 33
print("C") if c > d else print("=") if c == d else print("D")