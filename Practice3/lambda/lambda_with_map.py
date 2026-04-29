numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)
# [2, 4, 6, 8, 10]

names = ["Alice", "Bob", "Charlie"]
upper_names = list(map(lambda x: x.upper(), names))
print(upper_names)
# ['ALICE', 'BOB', 'CHARLIE']

ages = [("Alice", 25), ("Bob", 30), ("Charlie", 22)]
names_only = list(map(lambda x: x[0], ages))
print(names_only)
# ['Alice', 'Bob', 'Charlie']

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)
# [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]
diff = list(map(lambda x: x - 10, numbers))
print(diff)
# [-9, -8, -7, -6, -5]