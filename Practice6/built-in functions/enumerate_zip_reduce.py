# enumerate(iterable, start)
disciplines = ["Calc", "PP1", "Socio"]
disc = enumerate(disciplines)
for i, name in disc:
    print(i, name)

fruits = ["apple","banana","orange"]
fr = enumerate(fruits, start = 1):
for index, fruit in fr:
    print(f"{index}: {fruit}")

let = ["A", "B", "C"]
l = list(enumerate(a))
print(r)

# zip(iterator1, iterator2, iterator3 ...)
names = ["Asan","Charli","Bjork"]
scores = [85,90,78]
for name, score in zip(names, scores):
    print(name, score)

person1 = ("John", "Charles", "Mike")
person2 = ("Jenny", "Christy", "Monica", "Vicky")
x = zip(person1, person2)
for p1, p2 in x:
    print(p1, p2)

# Type checking
x = 5
print(type(x))

a = "10"
b = int(a)
print(b)

num = 5
text = str(num)
print(text)

x = 5.7
print(int(x))