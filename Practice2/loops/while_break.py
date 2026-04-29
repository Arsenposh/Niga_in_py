# Break the while loop
# Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# Output: 1
#         2
#         3

i = 0
while i < 6:
    print(i)
    if i == 4:
        break
    i += 1
# Output: 0
#         1
#         2
#         3


sum = 0
i = 0
while i < 10:
    sum += i
    if i == 5:
        break
    i += 1
print("Sum:", sum)
# Output: Sum: 15


# Continue the loop
# Continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Output: 1
#         2
#         4
#         5

i = 0
while i < 6:
    i += 1
    if i % 2 != 0:
        continue
    print(i)
# Output: 2
#         4

sum = 0
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    sum += i
print("Sum of even numbers:", sum)
# Output: Sum of even numbers: 30