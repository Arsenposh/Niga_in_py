# *args and **kwargs allow functions to accept a unknown number of arguments.

# Arbitrary arguments (*args) allows a function to accept any number of positional arguments.
def youngest(*kids):
  print("The youngest child is " + kids[2])
youngest("Emil", "Tobias", "Linus")


def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total
print(add_all(2, 3, 5))


def words(*args):
    return " ".join(args)
print(join_words("I", "love", "Programming", "Principles", "2"))


def hell_function(greeting, *names):
  for name in names:
    print(greeting, name)
my_function("Hello", "Emil", "Tobias", "Linus")

# The **kwargs parameter allows a function to accept any number of keyword arguments.

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)
my_function(name = "Tobias", age = 30, city = "Bergen")
# Type: <class 'dict'>
# Name: Tobias
# Age: 30
# All data: {'name': 'Tobias', 'age': 30, 'city': 'Bergen'}

def info(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)
info("emil123", age = 25, city = "Oslo", hobby = "coding")
# Username: emil123
# Additional details:
# age: 25
# city: Oslo
# hobby: coding

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")
# Title: User Info
# Positional arguments: ('Emil', 'Tobias')
# Keyword arguments: {'age': 25, 'city': 'Oslo'}