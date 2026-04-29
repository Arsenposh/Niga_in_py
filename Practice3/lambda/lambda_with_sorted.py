students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
# [('Tobias', 22), ('Emil', 25), ('Linus', 28)]

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)
# [1, 2, 5, 5, 6, 9]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
sorted_fruits = sorted(fruits, key=lambda x: len(x))
print(sorted_fruits)
# ['kiwi', 'mango', 'apple', 'banana', 'cherry']

words = ["apple", "banana", "kiwi", "grape"]
sorted_words = sorted(words, key=lambda x: x[-1])
print(sorted_words)
# ['banana', 'grape', 'kiwi', 'apple']

pairs = [(1, 2), (3, 1), (0, 5)]
sorted_pairs = sorted(pairs, key=lambda x: x[0] + x[1])
print(sorted_pairs)
# [(0, 5), (1, 2), (3, 1)]