# While loops
# Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1
# Output: 1
#         2
#         3
#         4
#         5

i = 0
sum = 0
while i < 5:
    sum += i
    i += 1
print("Sum:", sum)
# Output: Sum: 10

i = 3
while i > 0:
    print(i)
    i -= 1
# Output: 3
#         2
#         1

 
# Else statement in while loop
# Print a message once the condition is false:
i = 1
while i < 6:
  print(i)
  i += 1
else:
    print("i is no longer less than 6")
# Output: 1
#         2
#         3
#         4
#         5
#         i is no longer less than 6