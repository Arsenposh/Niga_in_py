numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
# [1, 3, 5, 7]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
short_fruits = list(filter(lambda x: len(x) < 6, fruits))
print(short_fruits)
# ['apple', 'kiwi', 'mango']

ages = [("John", 25), ("Jane", 30), ("Doe", 22), ("Smith", 28)]
adults = list(filter(lambda x: x[1] >= 25, ages))
print(adults)
# [('John', 25), ('Jane', 30), ('Smith', 28)]

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]

words = ["hello", "world", "python", "lambda", "filter"]
o = list(filter(lambda w: "o" in w, words))
print(o)
# ['hello', 'world', 'python']