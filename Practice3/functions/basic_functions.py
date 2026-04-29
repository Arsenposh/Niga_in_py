# A function helps avoiding code repetition.

# To call a function, write its name followed by parentheses:
def my_function():
  print("Hello from a function")

my_function()


def hello():
    print("Hello, world!")

hello()


def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))

def Power_func(a, b):
    print(a**b)

Power_func(3, 2)


def Is_even(a):
    return True if a % 2 == 0 else return False

print(Is_even(5))


def reverse_text(text):
    return text[::-1]

print(reverse_text("hello, World"))
