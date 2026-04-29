# With the continue we can stop the current iteration of the loop, and continue with the next:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
# Output: apple
#         cherry

for i in range(1, 7):
    if i % 2 != 0:
        continue
    print(i)
# Output: 2
#         4
#         6

num = [2, 3, 5, 7, 11, 13, 17, 19]
for n in num:
    if n > 10:
        continue
    print(n)
# Output: 2
#         3
#         5
#         7

num = [-2, 3, -5, 7, -11, 13, -17, 19]
for n in num:
    if n < 0:
        continue
    print("Positive number:", n)
# Output: Positive number: 3
#         Positive number: 7
#         Positive number: 13
#         Positive number: 19

for i in range(1, 10):
    if i%2 == 0:
        continue
    print(i)
# Output: 1
#         3
#         5
#         7
#         9