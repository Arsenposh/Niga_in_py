# map(function, iterables)
def fun(a, b):
  return a+b
x = map(func, ('11', '65', '123'), ('037', '56', '321'))

nums = [1, 2, 3, 4, 5]
x = map(lambda x: x*x, nums)
for i in x:
    print(i)

numbers = list(map(int, input().split()))
for i in numbers:
    print(i)

# filter(function, iterable)
ages = [5, 12, 17, 18, 24, 32]
def fun(x):
  if x<18:
    return False
  else:
    return True
adults = filter(myFunc, ages)
for x in adults:
    print(x)

numbers = [1,2,3,4,5,6]
even = filter(lambda x: x % 2 == 0, numbers)
for ev in even:
    print(ev)

words = ["calculus2", "programming", "history", "structures"]
long = filter(lambda a: len(a)>6, words)
for l in long:
    print(l)

# reduce(function, iterable) 
from functools import reduce

nums = [2, 4, 6, 8]
res = reduce(lambda x, y: x + y, nums)
print(res)

nums = [5, 9, 3, 12, 7]
res = reduce(lambda x, y: x if x > y else y, nums)
print(res)


