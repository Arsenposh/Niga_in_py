# With the break statement we can stop the loop before it has looped through all the items:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# Output: 1
#         2
#         3

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
# Output: apple
#         banana

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
# Output: apple

sum = 0
i = 0
while i < 10:
    sum += i
    if i == 5:
        break
    i += 1
print("Sum:", sum)
# Output: Sum: 15

for i in range(1, 10):
    if i % 2 == 0:
        print("First even number:", i)
        break
# Output: First even number: 2

passwords = ["123", "234", "789", "456"]
for i in passwords:
    if i == "456":
        print("Password found:", i)
        break
# Output: Password found: 456