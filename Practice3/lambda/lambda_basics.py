# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax:
# lambda arguments: expression

x = lambda a : a + 10
print(x(5))
# 15


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
# 13


def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
# 22
# 33

def calculator(a, b):
    return lambda c : (a+b)*c
lam = calculator(2,3)
print(lam(5))


sentence = lambda s1, s2: s1 + " " + s2
print(sentence("Hello", "World")) 