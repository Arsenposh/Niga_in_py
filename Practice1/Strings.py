# Assign String to a Variable
a = "Hello"
print(a)

# Multiline String
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# String Indexing
a = "Hello, World!"
print(a[1])  # e

# Slicing
b = "Hello, World!"
print(b[2:5])  # llo

# Negative Indexing
c = "Hello, World!"
print(c[-5:-2])  # orl

# String Length
d = "Hello, World!"
print(len(d))  # 13

# String Methods
e = "hello, world!"

# Check string
txt = "The best things in life are free!"
print("free" in txt) # True

# Check if not
txt = "The best things in life are free!"
print("expensive" not in txt) # True

#Slicing Strings
b = "Hello, World!"
print(b[2:5])  # llo
print(b[:5])   # Hello

#Negative Indexing
c = "Hello, World!"
print(c[-5:-2])  # orl
print(c[-5:])    # orld!
print(c[:-2])    # Hello, Worl

#Uppercase
f = "hello, world!"
print(f.upper())  # HELLO, WORLD!

# Lowercase
g = "HELLO, WORLD!"
print(g.lower())  # hello, world!

# Remove Whitespace
h = "   Hello, World!   "
print(h.strip())  # "Hello, World!"

#Split String
i = "Hello, World!"
print(i.split(","))  # ['Hello', ' World!']

#String Concatenation
j = "Hello"
k = "World"
print(j + " " + k)  # Hello World

#String Format
name = "John"
age = 36
txt = "My name is {}, and I am {}"
print(txt.format(name, age))  # My name is John, and I am 36

#Placeholder
quantity = 3
itemno = 5
price = 50.00
myorder = "
I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# I want 3 pieces of item 5 for 50.00 dollars.

#Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)  # We are the so-called "Vikings" from the north.

#\' Single Quote
#\\ Backslash
#\n New Line
#\r Carriage Return
#\t Tab
#\b Backspace
#\f Form Feed
#\ooo Octal value
#\xhh Hex value