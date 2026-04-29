# For loops
# Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# Output: apple
#         banana
#         cherry

# Loop through a string:
for x in "apple":
    print(x)
# Output: a
#         p
#         p
#         l
#         e

# The range() function returns a sequence of numbers, from 0 and increments by 1, and ends at a specified number.
for x in range(6):
    print(x)
# Output: 0
#         1
#         2
#         3
#         4
#         5

sum = 0
for x in range(10):
    sum += x
print("Sum:", sum)
# Output: Sum: 45

# It is possible to specify the increment value by adding a third parameter:
for x in range(2, 15, 3):
    print(x)
# Output: 2
#         5
#         8
#         11
#         14 

sum = 0
for x in range(1, 20, 2):
    sum += x
print("Sum of odd numbers:", sum)
# Output: Sum of odd numbers: 100

# The else in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
  print(x)
else:
  print("Finally finished!")
# Output: 0
#         1
#         2
#         3
#         4
#         5
#         Finally finished!

# Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
# Output: red apple
#         red banana
#         red cherry
#         big apple
#         big banana
#         big cherry
#         tasty apple
#         tasty banana
#         tasty cherry

for x in range(1, 4):
    for y in range(1, 4):
        print(x, y)
# Output: 1 1
#         1 2
#         1 3
#         2 1
#         2 2
#         2 3
#         3 1
#         3 2
#         3 3

# Pass statement
for x in [0, 1, 2]:
    pass
# Output: no output ( having an empty for loop like this, would raise an error without the pass statement )
